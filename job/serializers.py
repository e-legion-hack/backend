from rest_framework import serializers

from employee.models import Employee
from employee.serializers import EmployeeSerializer
from job.models import Task, Project
from utils.serializers import SerializerSaver


class BaseTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ('created_at', 'updated_at')


class ReadTaskSerializer(BaseTaskSerializer):
    creator = EmployeeSerializer()
    executors = EmployeeSerializer(many=True)


class CreateTaskSerializer(BaseTaskSerializer, SerializerSaver):
    creator = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all())
    executors = serializers.PrimaryKeyRelatedField(many=True, queryset=Employee.objects.all())


class BaseProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('created_at', 'updated_at')


class ReadProjectSerializer(BaseProjectSerializer):
    tasks = ReadTaskSerializer(many=True)


class CreateProjectSerializer(BaseProjectSerializer, SerializerSaver):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
