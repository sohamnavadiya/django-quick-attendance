# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from .models import SabhaType, SabhaSession, Attendance
from .serializers import SabhaTypeSerializer, SabhaSessionSerializer, AttendanceSerializer, AttendanceInsertSerializer
from rest_framework import generics, status


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


class AttendanceList(APIView):
    serializer_class = AttendanceInsertSerializer

    def post(self, request):
        attendance_obj = request.data.get('attendance', {})

        for single_user in attendance_obj:
            print single_user
            session_id = single_user.get('session_id')
            user_id = single_user.get('user')

            # The create serializer, validate serializer, save serializer pattern
            # below is common and you will see it a lot throughout this course and
            # your own work later on. Get familiar with it.
            serializer = self.serializer_class(data=single_user)
            try:
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except IntegrityError as error:
                print "Session not available"
                print error
            except ValidationError as error:
                print error
                # In this case, if the Person already exists, its name is updated
                single_obj = Attendance.objects.get(session_id=session_id, user=user_id)
                serializer = AttendanceInsertSerializer(single_obj, data=single_user)
                if serializer.is_valid():
                    print "Update existing attendance model."
                    serializer.save()

        return Response({"message": "Attendance stored successfully."}, status=status.HTTP_201_CREATED)


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
