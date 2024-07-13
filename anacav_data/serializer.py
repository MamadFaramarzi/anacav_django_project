from rest_framework import serializers
from.models import Test


class DataSerializer(serializers.Serializer):
    file = serializers.FileField()


class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['city','code','year','month','in_process','condition1','condition2','Condition3','total_condition']

