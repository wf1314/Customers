from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add$', CartAdd.as_view(),name='add'), # 添加购物车
    url(r'^info$', CartInfo.as_view(),name='info'), # 购物车主页面
    url(r'^update$', CartUpdate.as_view(),name='update'), # 更新购物车内商品信息
    url(r'^delete$', CartDelete.as_view(),name='delete'), # 删除购物车内商品
]
