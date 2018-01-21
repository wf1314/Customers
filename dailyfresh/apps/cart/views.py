from django.shortcuts import render
from django.views.generic import View
from apps.goods.models import *
from django.http import JsonResponse
from django_redis import get_redis_connection


# Create your views here.

class CartAdd(View):
    def post(self, request):

        user = request.user
        if not user.is_authenticated():
            return JsonResponse({'res': 6, 'errmes': '用户未登录'})
        # 获取传入的商品id
        sku_id = request.POST.get('sku_id')
        # 获取用户添加购物车的数量
        count = request.POST.get("count")

        if not all([sku_id, count]):
            return JsonResponse({'res': 0, 'errmes': '数据不完整'})

        try:
            # 通过商品id获取商品的sku对象
            sku = GoodsSku.objects.get(id=sku_id)
        except GoodsSku.DoesNotExist:
            return JsonResponse({'res': 1, 'errmes': '商品id不存在'})

        try:
            # 将传入值转换为整数
            count = int(count)
        except:
            return JsonResponse({'res': 2, 'errmes': '商品數量必须为正整数'})

        if count < 1:
            return JsonResponse({'res': 3, 'errmes': '数量不能小于1件'})
        # 从redis中读取存入的购物车信息
        conn = get_redis_connection('default')
        # 拼接redis中存储的购物车的key
        cart_key = 'cart_%d' % user.id
        # 获取存取的值,如果有返回该值,如果没有返回None
        cart_count = conn.hget(cart_key, sku_id)

        # print(int(cart_count))
        # 如果数据库中有数据则进行叠加
        if cart_count:
            count += int(cart_count)
        # 如果添加数量大于库存返回json
        if count > sku.goods_stock:
            return JsonResponse({'res': 4, 'errmes': '数量不能大于库存'})

        # 设置redis中存储的值,如果有则修改,无则添加
        conn.hset(cart_key, sku_id, count)
        # 获取购物车内订单的数量
        cart_num = conn.hlen(cart_key)

        return JsonResponse({'res': 5, 'sucmes': '购物车添加成功', 'cart_num':cart_num})


class CartInfo(View):

    def get(self,request):

        user = request.user
        # 创建redis对象
        conn = get_redis_connection('default')

        cart_key = 'cart_%d' %user.id
        # 获取redis中的哈希的属性与值返回一个字典
        all_cart = conn.hgetall(cart_key)

        skus = []
        all_count = 0
        all_price = 0

        # 便利字典通过items回去字典的视图对象
        for sku_id,count in all_cart.items():
            # 获取购物车内商品id 的对应商品对象
            sku = GoodsSku.objects.get(id=sku_id)
            # 给sku对象增加属性count用于记录用户添加的商品数量
            sku.count = int(count)
            # 增加count_price属性用于记录用户商品的小计
            sku.count_price = int(count)*sku.goods_price
            # print(sku.count_price)
            # 将对象添加至了列表
            skus.append(sku)
            # 累加计算添加商品的总数量
            all_count += int(count)
            # 累加计算添加商品的总价格
            all_price += sku.count_price

        context = {
            'skus':skus,
            'all_count':all_count,
            'all_price':all_price
        }


        return render(request,'cart/cart.html',context)


class CartUpdate(View):

    def post(self,request):

        user = request.user
        if not user.is_authenticated():
            return JsonResponse({'res': 6, 'errmes': '用户未登录'})
        # 获取传入的商品id
        sku_id = request.POST.get('sku_id')
        # 获取用户添加购物车的数量
        count = request.POST.get("count")

        if not all([sku_id, count]):
            return JsonResponse({'res': 0, 'errmes': '数据不完整'})

        try:
            # 通过商品id获取商品的sku对象
            sku = GoodsSku.objects.get(id=sku_id)
        except GoodsSku.DoesNotExist:
            return JsonResponse({'res': 1, 'errmes': '商品id不存在'})

        try:
            # 将传入值转换为整数
            count = int(count)
        except:
            return JsonResponse({'res': 2, 'errmes': '商品數量必须为正整数'})

        if count < 1:
            return JsonResponse({'res': 3, 'errmes': '数量不能小于1件'})
        # 从redis中读取存入的购物车信息
        conn = get_redis_connection('default')
        # 拼接redis中存储的购物车的key
        cart_key = 'cart_%d' % user.id

        if count > sku.goods_stock:

            return JsonResponse({'res': 4, 'errmes': '商品库存不足'})

        conn.hset(cart_key,sku_id,count)

        all_count = 0
        for i in conn.hvals(cart_key):

            all_count += int(i)

        return JsonResponse({'res': 5, 'all_count':all_count,'sucmes': '更新购物车成功'})


class CartDelete(View):

    def post(self,request):

        user = request.user
        if not user.is_authenticated():
            return JsonResponse({'res': 6, 'errmes': '用户未登录'})
        # 获取传入的商品id
        sku_id = request.POST.get('sku_id')

        if not all([sku_id]):
            return JsonResponse({'res': 0, 'errmes': '数据不完整'})

        try:
            # 通过商品id获取商品的sku对象
            sku = GoodsSku.objects.get(id=sku_id)
        except GoodsSku.DoesNotExist:
            return JsonResponse({'res': 1, 'errmes': '商品id不存在'})

        # 从redis中读取存入的购物车信息
        conn = get_redis_connection('default')
        # 拼接redis中存储的购物车的key
        cart_key = 'cart_%d' % user.id

        conn.hdel(cart_key,sku_id)

        all_count = 0
        for i in conn.hvals(cart_key):
            all_count += int(i)


        return JsonResponse({'res': 5,  'all_count':all_count,'sucmes': '删除成功'})


