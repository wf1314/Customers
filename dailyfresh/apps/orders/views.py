from django.shortcuts import render
from django.views.generic import View
from utils.base_view import MyRequired
from django.http import HttpResponse, JsonResponse
from .models import *
from apps.goods.models import *
from apps.users.models import *
from django_redis import get_redis_connection
from datetime import datetime
from django.db import transaction


# Create your views here.

class Place(MyRequired, View):
    def post(self, request):
        user = request.user
        # 获取一个key对应的多个值
        sku_ids = request.POST.getlist('sku_ids')

        # print(sku_ids)
        # 获取当前用户的地址对象
        addrs = Address.objects.filter(User_id=user)
        # 链接redis
        conn = get_redis_connection('default')
        cart_key = 'cart_%d' % user.id

        skus = []
        all_count = 0
        all_price = 0
        # 遍历商品id
        for sku_id in sku_ids:
            # 获取对应商品对象
            sku = GoodsSku.objects.get(id=sku_id)
            # 从redis中查询出购物车中商品的数量
            count = conn.hget(cart_key, sku_id)
            # print(sku.goods_price)
            # 计算出小计的价格
            samll_price = sku.goods_price * int(count)
            # 将数量转换为整数并添加为sku的属性
            sku.count = int(count)
            # 　添加属性，小计
            sku.samll_price = samll_price
            # 讲ｓｋｕ对象添加到列表中
            skus.append(sku)
            # 累加计算总价格和总数量
            all_count += int(count)
            all_price += samll_price

        # 默认运费
        freight = 10
        # 将列表转换为字符串
        sku_ids = ','.join(sku_ids)

        # 运费加商品总价
        pay_money = freight + all_price
        context = {
            'addrs': addrs,
            'skus': skus,
            'freight': freight,
            'all_count': all_count,
            'all_price': all_price,
            'pay_money': pay_money,
            'sku_ids': sku_ids
        }

        return render(request, 'orders/place_order.html', context)


class CommitView1(MyRequired, View):
    """悲观锁"""
    @transaction.atomic
    def post(self, request):
        user = request.user
        # 获取ajax传入地址id
        addr_id = request.POST.get('addr_id')
        # 获取ajax传入的支付方式
        pay_style = request.POST.get('pay_style')
        # 获取ajax传入的商品id
        sku_ids = request.POST.get('sku_ids')

        if not all([addr_id, pay_style, sku_ids]):
            return JsonResponse({'res': 1, 'errmes': '信息不完整'})
        # print(addr_id)
        try:
            # 获取地址对象

            addr = Address.objects.get(id=addr_id)
        except:
            return JsonResponse({'res': 2, 'errmes': '收货地址有误'})
        # print(3)
        if pay_style not in Order_mes.pay_dict.keys():
            return JsonResponse({'res': 3, 'errmes': '支付方式有误'})
        # 构造订单id
        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + str(user.id)
        # print(order_id)
        total_count = 0
        total_price = 0
        transport_price = 10
        # user_id = user
        # addr_id = addr
        # 创建订单数据,添加至数据库

        sid = transaction.savepoint()
        try:
            order = Order_mes.objects.create(order_id=order_id,
                                             pay_way=pay_style,
                                             user_id=user,
                                             addr_id=addr,
                                             transport_price=transport_price,
                                             total_count=total_count,
                                             total_price=total_price)
            # 将传入的id用,分割为列表
            sku_ids = sku_ids.split(',')
            # print(sku_ids)
            # 创建redis对象
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id

            for sku_id in sku_ids:
                try:
                    # 获取商品对象
                    sku = GoodsSku.objects.select_for_update().get(id=sku_id)
                    # sku = GoodsSku.objects.get(id=sku_id)
                except:
                    transaction.savepoint_rollback(sid)

                    return JsonResponse({'res': 4, 'errmes': '商品id不存在'})
                # 获取对应商品在购物车中的数量
                goods_count = conn.hget(cart_key, sku_id)
                # 获取商品的价格
                goods_price = sku.goods_price
                # print(goods_count)
                # print(goods_price)
                # print(order_id)
                # print(sku)
                if int(goods_count) > sku.goods_stock:
                    transaction.savepoint_rollback(sid)
                    return JsonResponse({'res': 8, 'errmes': '库存不足'})
                # 创建订单商品表
                OrderGoods.objects.create(goods_count=int(goods_count),
                                          goods_price=goods_price,
                                          order_mes_id=order,
                                          goods_sku_id=sku)
                # print(11111)
                # 库存减1 销量+1

                sku.goods_stock -= int(goods_count)

                sku.goods_annul += int(goods_count)
                sku.save()

                # 计算商品总数量
                total_count += int(goods_count)
                # 计算商品总价格
                total_price += goods_price * int(goods_count)
            # print(2)

            # 更新订单表的数量和价格属性
            order.total_count = total_count
            order.total_price = total_price
            order.save()
            # 从购物车中删除
            conn.hdel(cart_key, *sku_ids)
        except Exception as e:
            transaction.savepoint_rollback(sid)
            return JsonResponse({'res': 7, 'sucmes': '订单创建失败'})
        return JsonResponse({'res': 5, 'sucmes': '订单创建成功'})

class CommitView(MyRequired, View):
    """乐观锁"""
    @transaction.atomic
    def post(self, request):
        user = request.user
        # 获取ajax传入地址id
        addr_id = request.POST.get('addr_id')
        # 获取ajax传入的支付方式
        pay_style = request.POST.get('pay_style')
        # 获取ajax传入的商品id
        sku_ids = request.POST.get('sku_ids')

        if not all([addr_id, pay_style, sku_ids]):
            return JsonResponse({'res': 1, 'errmes': '信息不完整'})
        # print(addr_id)
        try:
            # 获取地址对象
            addr = Address.objects.get(id=addr_id)

        except:
            return JsonResponse({'res': 2, 'errmes': '收货地址有误'})
        # print(3)
        if pay_style not in Order_mes.pay_dict.keys():
            return JsonResponse({'res': 3, 'errmes': '支付方式有误'})
        # 构造订单id
        order_id = datetime.now().strftime('%Y%m%d%H%M%S') + str(user.id)
        # print(order_id)
        total_count = 0
        total_price = 0
        transport_price = 10
        # user_id = user
        # addr_id = addr
        # 创建订单数据,添加至数据库

        sid = transaction.savepoint()
        try:
            order = Order_mes.objects.create(order_id=order_id,
                                             pay_way=pay_style,
                                             user_id=user,
                                             addr_id=addr,
                                             transport_price=transport_price,
                                             total_count=total_count,
                                             total_price=total_price)
            # 将传入的id用,分割为列表
            sku_ids = sku_ids.split(',')
            # print(sku_ids)
            # 创建redis对象
            conn = get_redis_connection('default')
            cart_key = 'cart_%d' % user.id
            print(123)
            for sku_id in sku_ids:
                for i in range(3):
                    try:
                        # 获取商品对象
                        sku = GoodsSku.objects.get(id=sku_id)
                    except:
                        transaction.savepoint_rollback(sid)

                        return JsonResponse({'res': 4, 'errmes': '商品id不存在'})
                    # 获取对应商品在购物车中的数量
                    goods_count = conn.hget(cart_key, sku_id)
                    # 获取商品的价格
                    goods_price = sku.goods_price

                    if int(goods_count) > sku.goods_stock:
                        transaction.savepoint_rollback(sid)

                        return JsonResponse({'res':8,'errmes':'库存不足'})


                    # 创建订单商品表
                    old_stock = sku.goods_stock
                    new_stock = old_stock - int(goods_count)
                    new_annul = sku.goods_annul+ int(goods_count)
                    res = GoodsSku.objects.filter(id=sku_id,goods_stock=old_stock).update(goods_stock=new_stock,goods_annul=new_annul)
                    if res == 0:
                        if i==2:
                            transaction.savepoint_rollback(sid)
                            return JsonResponse({'res': 7, 'sucmes': '订单创建失败'})
                        continue

                    OrderGoods.objects.create(goods_count=int(goods_count),
                                              goods_price=goods_price,
                                              order_mes_id=order,
                                              goods_sku_id=sku)



                    # 计算商品总数量
                    total_count += int(goods_count)
                    # 计算商品总价格
                    total_price += goods_price * int(goods_count)
                    # print(2)
                    break
            # 更新订单表的数量和价格属性
            order.total_count = total_count
            order.total_price = total_price
            order.save()
            # 从购物车中删除
            conn.hdel(cart_key, *sku_ids)

        except Exception as e:
            transaction.savepoint_rollback(sid)
            return JsonResponse({'res': 7, 'sucmes': '订单创建失败'})
        return JsonResponse({'res': 5, 'sucmes': '订单创建成功'})
