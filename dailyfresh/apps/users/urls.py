from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^register$', Register.as_view(),name='register'), # 注册视图
    url(r'^login$', Login.as_view(),name='login'), # 登录视图
    url(r'^logout$', Logout.as_view(),name='logout'), #退出登录视图
    url(r'^active/(?P<token>.*)$', Active.as_view(),name='token') # 激活链接视图
]
