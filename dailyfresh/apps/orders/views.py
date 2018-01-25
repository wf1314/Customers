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
from alipay import AliPay
from django.conf import settings


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
        if int(pay_style) not in Order_mes.pay_dict.keys():
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
            return JsonResponse({'res': 7, 'errmes': '订单创建失败'})
        return JsonResponse({'res': 5, 'sucmes': '订单创建成功'})


class OrderPay(View):

    def post(self,request):

        user = request.user
        # 如果用户未登录则返回错误信息
        print(111)
        if not user.is_authenticated():

            return JsonResponse({'res':0,'errmes':'用户未登录'})
        # 获取ajax传入的订单id
        order_id = request.POST.get('order_id')
        # 校验数据完整性
        if not all([order_id]):

            return  JsonResponse({'res':1,'errmes':'数据不完整'})

        try:
            # 获取订单对象
            order = Order_mes.objects.get(order_id=order_id,
                                            user_id=user,
                                            pay_way=3,
                                            pay_state=1)
        except Exception as e:

            return JsonResponse({'res':2,'errmes':'订单id有误'})
        # print(333)
        alipay = AliPay(
            appid="2016091300498944", # 应用id
            app_notify_url=None,  # 默认回调url
            app_private_key_path=settings.APP_PRIVATE_KEY_PATH,
            alipay_public_key_path=settings.APP_PUBLIC_KEY_PATH,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug=True # 默认False True
        )
        all_price = order.total_price +order.transport_price
        # 调用支付宝alipay.trade.page.pay的接口
        # 电脑网站支付，需要跳转到https://openapi.alipaydev.com/gateway.do? + order_string
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id,  # 订单id
            total_amount=str(all_price),  # 订单总金额
            subject='天天生鲜%s' % order_id,  # 订单标题
            return_url=None,
            notify_url=None  # 可选, 不填则使用默认notify url
        )
        pay_url = 'https://openapi.alipaydev.com/gateway.do?' + order_string


        return JsonResponse({'res':3,'pay_url':pay_url,'sucmes':'请求成功'})


class OrderCheck(View):
    def post(self, request):

        user = request.user
        # 如果用户未登录则返回错误信息
        # print(111)
        if not user.is_authenticated():
            return JsonResponse({'res': 0, 'errmes': '用户未登录'})
        # 获取ajax传入的订单id
        order_id = request.POST.get('order_id')
        # 校验数据完整性
        if not all([order_id]):
            return JsonResponse({'res': 1, 'errmes': '数据不完整'})

        try:
            # 获取订单对象
            order = Order_mes.objects.get(order_id=order_id,
                                          user_id=user,
                                          pay_way=3,
                                          pay_state=1)
        except Exception as e:

            return JsonResponse({'res': 2, 'errmes': '订单id有误'})

        alipay = AliPay(
            appid="2016091300498944",  # 应用id
            app_notify_url=None,  # 默认回调url
            app_private_key_path=settings.APP_PRIVATE_KEY_PATH,
            alipay_public_key_path=settings.APP_PUBLIC_KEY_PATH,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
            sign_type="RSA2",  # RSA 或者 RSA2
            debug=True  # 默认False True
        )


        #         "trade_no": "2017032121001004070200176844", # 支付宝交易号
        #         "code": "10000", # 网关返回码 10000表示成功
        #         "invoice_amount": "20.00",
        #         "open_id": "20880072506750308812798160715407",
        #         "fund_bill_list": [
        #             {
        #                 "amount": "20.00",
        #                 "fund_channel": "ALIPAYACCOUNT"
        #             }
        #         ],
        #         "buyer_logon_id": "csq***@sandbox.com",
        #         "send_pay_date": "2017-03-21 13:29:17",
        #         "receipt_amount": "20.00",
        #         "out_trade_no": "out_trade_no15",
        #         "buyer_pay_amount": "20.00",
        #         "buyer_user_id": "2088102169481075",
        #         "msg": "Success",
        #         "point_amount": "0.00",
        #         "trade_status": "TRADE_SUCCESS",# 交易状态
        #         "total_amount": "20.00"
        #     },
        #     "sign": ""
        # }



        while True:
            # 查询支付状态 返回值为以上字典
            response = alipay.api_alipay_trade_query(out_trade_no=order_id)
            # print(response)
            # 获取返回值中的状态码 如果状态码为10000表示链接成功
            code = response.get('code')

            # print(response.get("trade_status"),code)
            if code == '10000' and response.get("trade_status") == 'TRADE_SUCCESS':
                # 符合此要求表示请求成功 获取支付编号 更改数据库中的订单数据
                trade_no = response.get('trade_no')
                # print('test')
                order.pay_state=4
                order.pay_no=trade_no
                order.save()
                # print('ee')
                return JsonResponse({'res':3,'sucmes':'支付成功'})
                #支付成功

            elif code == '40004' or (code == '10000' and response.get("trade_status") == 'WAIT_BUYER_PAY'):
                # 表示,未发起请求或者等待用户支付状态
                import time
                time.sleep(3)

                # 等待支付
                continue
            else:
                # 支付失败

                return JsonResponse({'res':4,'sucmess':'支付失败'})
