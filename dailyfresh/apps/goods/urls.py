from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', GoodsIndex.as_view(),name='index'), # 主页
    url(r'^detail/(?P<sku_id>\d+)$', Detail.as_view(),name='detail'), # 商品详情页
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(),name='list'), # 商品列表页(分类显示)
]
