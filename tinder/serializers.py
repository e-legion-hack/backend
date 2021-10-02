from rest_framework import serializers

from employee.models import Employee
from tinder.models import Activity


class BaseActivitySerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())

    class Meta:
        model = Activity
        exclude = ('created_at', )

