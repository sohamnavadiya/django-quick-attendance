from django.conf.urls import url
from . import views

urlpatterns = [
    # Sabha insertion, update, select APIs
    url(r'^sabha/$', views.SabhaTypeList.as_view()),
    url(r'^sabha/(?P<pk>[0-9]+)/$', views.SabhaTypeDetail.as_view()),

    # Session APIs
    url(r'^session/$', views.SabhaSessionList.as_view()),
    url(r'^session/(?P<pk>[0-9]+)/$', views.SabhaSessionDetail.as_view()),
    url(r'^session/(?P<sabhatype>\w+)/$', views.SabhaSessionByStatus.as_view()),

    # Attendance APIs
    url(r'^attendance/$', views.AttendanceList.as_view()),
    # url(r'^attendance/(?P<pk>[0-9]+)/$', views.AttendanceDetails.as_view()),
    url(r'^attendance/(?P<session_id>[0-9]+)/$', views.AttendanceDetail.as_view()),
]
