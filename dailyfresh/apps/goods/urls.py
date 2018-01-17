from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', GoodsIndex.as_view(),name='index')
]
