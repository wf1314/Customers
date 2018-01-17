from django.shortcuts import render
from django.views.generic import View
from .models import *
from django_redis import get_redis_connection

# Create your views here.

class GoodsIndex(View):
    def get(self, request):

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
        user = request.user
        # 如果用户已登录则查询redis数据库中存储的数量
        if user.is_authenticated():

            redis_con = get_redis_connection('default')
            cart_key = 'cart_%s' %user.id

            cart_count = redis_con.hlen(cart_key)



        content = {'goods_type':goods_type,
                   'good_activity':good_activity,
                   'sales':sales,
                   'cart_count':cart_count}

        return render(request, 'goods/index.html',content)
