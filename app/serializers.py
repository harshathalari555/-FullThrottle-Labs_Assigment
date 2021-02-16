from rest_framework import serializers
from .models import Member,ActivityPeriod
import pytz
from rest_framework import serializers
from timezone_field.rest_framework import TimeZoneSerializerField

class MemberSerializer(serializers.ModelSerializer):
    tz = TimeZoneSerializerField()



    class Meta:
        model = Member
        fields = '__all__'
        depth=1





class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time','end_time']

