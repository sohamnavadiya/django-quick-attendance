from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^sabha/$', views.SabhaTypeList.as_view()),
    url(r'^sabha/(?P<pk>[0-9]+)/$', views.SabhaTypeDetail.as_view()),

    url(r'^sabhasession/$', views.SabhaSessionList.as_view()),
    url(r'^sabhasession/(?P<pk>[0-9]+)/$', views.SabhaSessionDetail.as_view()),
    url(r'^sabhasession/(?P<sabhatype>\w+)/$', views.SabhaSessionByStatus.as_view()),
]
