from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^register$', Register.as_view(),name='register'), # 注册视图
    url(r'^login$', Login.as_view(),name='login'), # 登录视图
    url(r'^logout$', Logout.as_view(),name='logout'), #退出登录视图
    url(r'^active/(?P<token>.*)$', Active.as_view(),name='token'), # 激活链接视图
    url(r'^$', UserCenterInfo.as_view(), name='info'),  # 用户中心主页视图
    url(r'^order$', UserCenterOrder.as_view(), name='order'),  # 用户中心订单视图
    url(r'^site$', UserCenterSite.as_view(), name='site'),  # 用户中心收货地址视图

]
