from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', GoodsIndex.as_view(),name='index'),
    url(r'^detail/(?P<sku_id>\d+)$', Detail.as_view(),name='detail'),
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', ListView.as_view(),name='list'),
]
