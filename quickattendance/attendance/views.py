# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.settings import api_settings
from .models import SabhaType, SabhaSession, Attendance
from .serializers import SabhaTypeSerializer, SabhaSessionSerializer, AttendanceSerializer
from rest_framework import generics


class SabhaTypeList(generics.ListCreateAPIView):
    queryset = SabhaType.objects.all()
    serializer_class = SabhaTypeSerializer


class SabhaTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SabhaType.objects.all()
    serializer_class = SabhaTypeSerializer


class SabhaSessionList(generics.ListCreateAPIView):
    queryset = SabhaSession.objects.all()
    serializer_class = SabhaSessionSerializer


class SabhaSessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SabhaSession.objects.all()
    serializer_class = SabhaSessionSerializer


class SabhaSessionByStatus(generics.ListAPIView):
    serializer_class = SabhaSessionSerializer

    def get_queryset(self):
        """
        This view should return a list of all the sabha as determined by the sabhatype portion of the URL.
        """
        sabhatype = self.kwargs['sabhatype']
        return SabhaSession.objects.session(sabhatype)


class AttendanceList(generics.ListCreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer


class AttendanceDetail(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    pagination_class = api_settings.DEFAULT_PAGINATION_CLASS

    def get_queryset(self):
        """
        This view should return a list of all the USERS of particular session.
        """
        session_id = self.kwargs['session_id']
        return Attendance.objects.get_session_users(session_id)
