# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.views import APIView
from .models import SabhaType, SabhaSession
from .serializers import SabhaTypeSerializer, SabhaSessionSerializer
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
        return SabhaSession.objects.active_session(sabhatype)
