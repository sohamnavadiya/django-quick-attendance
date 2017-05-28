from attendance.models import SabhaSession, SabhaType, Attendance

from authentication.serializers import LoginSerializer

from authentication.models import User

from profiles.models import Profile

from authentication.serializers import UserSerializer

from authentication.serializers import DynamicFieldsModelSerializer
from rest_framework import serializers


class SabhaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SabhaType
        fields = ('id', 'sabha_type')


class SabhaSessionSerializer(DynamicFieldsModelSerializer):
    # sabhatype = SabhaTypeSerializer(read_only=True)

    class Meta:
        model = SabhaSession
        fields = ('id', 'user', 'sabhatype', 'date', 'status')
        # depth = 1


class AttendanceSerializer(serializers.ModelSerializer):
    # session_id = SabhaSessionSerializer(read_only=True)
    user = UserSerializer(read_only=True, fields=('username',))
    last_modified_by = UserSerializer(read_only=True, fields=('username',))

    # To change the key name in response
    session_info = SabhaSessionSerializer(read_only=True, source='session_id', fields=('id', 'sabhatype'))

    class Meta:
        model = Attendance
        fields = ('status', 'user', 'last_modified_by', 'session_info', 'leave_reason')
        # To add foreign key value info instead just primary key
        # depth = 1


class AttendanceInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('status', 'user', 'last_modified_by', 'session_id', 'leave_reason')
        # To add foreign key value info instead just primary key
        # depth = 1
