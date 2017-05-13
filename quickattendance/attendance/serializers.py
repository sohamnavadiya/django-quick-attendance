from attendance.models import SabhaSession, SabhaType
from rest_framework import serializers


class SabhaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SabhaType
        fields = ('id', 'sabha_type')


class SabhaSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SabhaSession
        fields = ('id', 'user', 'sabhatype', 'date', 'status')
