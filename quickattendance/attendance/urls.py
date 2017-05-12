from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sabha/$', views.SabhaTypeList.as_view()),
    url(r'^sabha/(?P<pk>[0-9]+)/$', views.SabhaTypeDetail.as_view()),
]
