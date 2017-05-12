from django.conf.urls import url
from . import views

from .views import ProfileRetrieveAPIView, ProfileFollowAPIView

urlpatterns = [
    url(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
    url(r'^profiles/(?P<username>\w+)/follow/?$', ProfileFollowAPIView.as_view()),

    url(r'^usertype/$', views.UserTypeList.as_view()),
    url(r'^usertype/(?P<pk>[0-9]+)/$', views.UserTypeDetail.as_view()),
]
