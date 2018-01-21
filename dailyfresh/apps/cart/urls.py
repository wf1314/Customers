from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^add$', CartAdd.as_view(),name='add'),
    url(r'^info$', CartInfo.as_view(),name='info'),
    url(r'^update$', CartUpdate.as_view(),name='update'),
    url(r'^delete$', CartDelete.as_view(),name='delete'),
]
