from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^remove/cancel$', views.start),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^remove/aprove/(?P<id>\d+)$', views.delete),
]