from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'^place$', Place.as_view(), name='place'),
    url(r'^commit$', CommitView.as_view(), name='commit')
]
