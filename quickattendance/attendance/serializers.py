from attendance.models import SabhaType
from rest_framework import serializers


class SabhaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SabhaType
        fields = ('id', 'sabha_type')
