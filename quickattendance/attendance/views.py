# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import SabhaType
from .serializers import SabhaTypeSerializer
from rest_framework import generics


class SabhaTypeList(generics.ListCreateAPIView):
    queryset = SabhaType.objects.all()
    serializer_class = SabhaTypeSerializer


class SabhaTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SabhaType.objects.all()
    serializer_class = SabhaTypeSerializer