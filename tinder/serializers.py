from rest_framework import serializers

from employee.models import Employee
from employee.serializers import EmployeeSerializer
from tinder.models import Activity
from utils.serializers import SerializerSaver


class BaseActivitySerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())

    class Meta:
        model = Activity
        exclude = ('created_at', )

