from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^place$', Place.as_view(), name='place'), # 订单提交页面显示
    url(r'^commit$', CommitView.as_view(), name='commit'), # 订单提交
    url(r'^pay$', OrderPay.as_view(), name='pay'), # 订单支付
    url(r'^check$', OrderCheck.as_view(), name='check') # 订单状态查询
]
