from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^register$', Register.as_view(),name='register'),
    url(r'^login$', Login.as_view(),name='login'),
    url(r'^active/(?P<token>.*)$', Active.as_view(),name='token')
    # url(r'^register_handle$', Register.as_view(),name='register_handle')
]
