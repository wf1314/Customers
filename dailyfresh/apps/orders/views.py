from django.shortcuts import render
from django.views.generic import View
from utils.base_view import MyRequired
from django.http import HttpResponse,JsonResponse
from .models import *
from apps.goods.models import *
from apps.users.models import *
from django_redis import get_redis_connection
from datetime import datetime

# Create your views here.

class Place(MyRequired,View):

    def post(self,request):

        user = request.user
        sku_ids = request.POST.getlist('sku_ids')

        print(sku_ids)

        addrs = Address.objects.filter(User_id=user)

        conn = get_redis_connection('default')
        cart_key = 'cart_%d' %user.id

        skus =[]
        all_count = 0
        all_price = 0

        for sku_id in sku_ids:

            sku = GoodsSku.objects.get(id=sku_id)

            count = conn.hget(cart_key,sku_id)
            print(sku.goods_price)
            samll_price = sku.goods_price * int(count)

            sku.count = int(count)
            sku.samll_price = samll_price

            skus.append(sku)

            all_count += int(count)
            all_price += samll_price



        freight = 10
        sku_ids = ','.join(sku_ids)


        pay_money = freight + all_price
        context = {
            'addrs':addrs,
            'skus':skus,
            'freight':freight,
            'all_count':all_count,
            'all_price':all_price,
            'pay_money':pay_money,
            'sku_ids':sku_ids
        }


        return render(request, 'orders/place_order.html',context)


class CommitView(MyRequired,View):

    def post(self,request):
        user = request.user
        addr_id = request.POST.get('addr_id')
        pay_style = request.POST.get('pay_style')
        sku_ids = request.POST.get('sku_ids')

        if not all([addr_id,pay_style,sku_ids]):

            return JsonResponse({'res':1, 'errmes':'信息不完整'})
        print(addr_id)
        try:
            addr = Address.objects.get(id=addr_id)
        except:
            return JsonResponse({'res':2,'errmes':'收货地址有误'})
        print(3)
        if pay_style not in Order_mes.pay_dict.keys():
            return JsonResponse({'res':3, 'errmes':'支付方式有误'})

        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + str(user.id)
        print(order_id)
        total_count = 0
        total_price = 0
        transport_price=10
        # user_id = user
        # addr_id = addr
        order = Order_mes.objects.create(order_id=order_id,
                                 pay_way=pay_style,
                                 user_id=user,
                                 addr_id=addr,
                                 transport_price=transport_price,
                                 total_count=total_count,
                                 total_price=total_price)

        sku_ids = sku_ids.split(',')
        print(sku_ids)
        conn = get_redis_connection('default')
        cart_key = 'cart_%d' %user.id

        for sku_id in sku_ids:
            try:
                sku = GoodsSku.objects.get(id=sku_id)
            except:
                return JsonResponse({'res':4,'errmes':'商品id不存在'})

            goods_count = conn.hget(cart_key,sku_id)
            goods_price = sku.goods_price
            print(goods_count)
            print(goods_price)
            print(order_id)
            print(sku)
            OrderGoods.objects.create(goods_count=int(goods_count),
                                      goods_price=goods_price,
                                      order_mes_id=order,
                                      goods_sku_id=sku)
            print(11111)
            sku.goods_stock -= int(goods_count)
            sku.goods_annul += int(goods_count )

            total_count += int(goods_count)
            total_price += goods_price*int(goods_count)
        print(2)

        order.total_count = total_count
        order.total_price = total_price
        order.save()

        conn.hdel(cart_key,*sku_ids)

        return JsonResponse({'res':5,'sucmes':'订单创建成功'})