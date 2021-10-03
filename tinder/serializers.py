from rest_framework import serializers

from employee.models import Employee
from tinder.models import Activity, LikedActivity
from utils.serializers import SerializerSaver


class BaseActivitySerializer(serializers.ModelSerializer, SerializerSaver):
    creator = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())

    class Meta:
        model = Activity
        exclude = ('created_at', )


class ActivityLikedSerializer(serializers.ModelSerializer, SerializerSaver):
    activity = serializers.PrimaryKeyRelatedField(queryset=Activity.objects.all())
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())

    class Meta:
        model = LikedActivity
        exclude = ('created_at', )

    def create(self, validated_data):
        instance, _ = LikedActivity.objects.get_or_create(
            activity=validated_data['activity'],
            employee=validated_data['employee'],
        )
        return instance
