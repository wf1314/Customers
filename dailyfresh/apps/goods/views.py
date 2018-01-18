from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
from apps.orders.models import *
from django_redis import get_redis_connection
from django.core.cache import cache
from django.core.urlresolvers import reverse




# Create your views here.

class GoodsIndex(View):
    def get(self, request):

        content = cache.get('index_data')



        if content is None:

            print('设置缓存成功')
            # 获取商品分类表的查询集对象
            goods_type = GoodsType.objects.all()
            # 获取首页图片轮播表查询集对象并按index排序
            good_activity = GoodsImgActivity.objects.all().order_by('Activity_img_index')
            # 获取促销活动表查询集对象
            sales = SalesPromotion.objects.all().order_by('promotion_index')
            # 获取商品分类对象
            for good in goods_type:
                # 通过商品分类对象向商品分类表中增加两个新的属性
                wenzi = GoodsTypeShow.objects.filter(goods_type_id=good,show_type=0).order_by('show_index')
                photo = GoodsTypeShow.objects.filter(goods_type_id=good,show_type=1).order_by('show_index')

                good.wenzi = wenzi
                good.photo = photo
            # 未登录用户购物车默认显示为0
            cart_count = 0
            content = {'goods_type':goods_type,
                       'good_activity':good_activity,
                       'sales':sales,
                       'cart_count':cart_count}

            cache.set('index_data', content, 3600)

        user = request.user
        # 如果用户已登录则查询redis数据库中存储的数量
        if user.is_authenticated():

            redis_con = get_redis_connection('default')
            cart_key = 'cart_%s' %user.id

            cart_count = redis_con.hlen(cart_key)

            content.update(cart_count=cart_count)


        return render(request, 'goods/index.html',content)


class Detail(View):

    def get(self,request, sku_id):

        #查询商品分类
        types = GoodsType.objects.all()

        # 获取传入id的商品sku信息
        try:
            sku = GoodsSku.objects.get(id=sku_id)
        except GoodsSku.DoesNotExist:

            return redirect(reverse('goods:index'))

        # 评论
        comment = OrderGoods.objects.filter(goods_sku_id=sku).exclude(goods_comment='').order_by('-update_time')
        # 与该商品同类的两条商品信息
        same_type_goods = GoodsSku.objects.filter(goods_type_id=sku.goods_type_id).order_by('-update_time')[:2]
        # 获取相同spu的其他商品
        same_spu_skus = GoodsSku.objects.filter(goods_spu_id=sku.goods_spu_id).exclude(id=sku.id)
        cart_count = 0
        user = request.user
        # 如果用户已登录则查询redis数据库中存储的数量
        if user.is_authenticated():
            redis_con = get_redis_connection('default')
            cart_key = 'cart_%s' % user.id

            cart_count = redis_con.hlen(cart_key)

            history_key = 'history_%s' %user.id

            redis_con.lrem(history_key,0,sku_id)

            redis_con.lpush(history_key,sku_id)

            redis_con.ltrim(history_key,0,4)

        content = {
            'types':types,
            'sku':sku,
            'comment':comment,
            'same_type_goods' : same_type_goods,
            'same_spu_skus':same_spu_skus,
            'cart_count':cart_count
        }

        return render(request, 'goods/detail.html', content)


class ListView(View):

    def get(self,request,type_id,page):

        goods_type = GoodsType.objects.all()

        try:
            type = GoodsType.objects.get(id=type_id)


        except GoodsType.DoesNotExist:

            return redirect(reverse('goods:index'))
        sort = request.GET.get('sort')

        if sort == 'price':
            goods_list = GoodsSku.objects.filter(goods_type_id=type).order_by('goods_price')

        elif sort == 'annul':
            goods_list = GoodsSku.objects.filter(goods_type_id=type).order_by('-goods_annul')

        else:
            sort = 'default'
            goods_list = GoodsSku.objects.filter(goods_type_id=type).order_by('-id')

        from django.core.paginator import Paginator

        paginat = Paginator(goods_list,2)

        page_data = paginat.page(page)


        same_type_goods = GoodsSku.objects.filter(goods_type_id=type).order_by('-update_time')[:2]

        cart_count = 0
        user = request.user
        # 如果用户已登录则查询redis数据库中存储的数量
        if user.is_authenticated():

            redis_con = get_redis_connection('default')
            cart_key = 'cart_%s' % user.id

            cart_count = redis_con.hlen(cart_key)

            history_key = 'history_%s' %user.id

        content = {
            'goods_type':goods_type,
            'type':type,
            'page_data':page_data,
            'same_type_goods':same_type_goods,
            'cart_count':cart_count,
            'sort':sort
        }

        return render(request, 'goods/list.html',content)