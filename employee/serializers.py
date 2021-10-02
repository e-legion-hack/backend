from rest_framework import serializers

from employee.models import Employee
from office.serializers import DepartamentSerializer, OfficeSerializer
from utils.enums import EmployeeStatus, RomeStatus


class SubEmployeeSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    rome_status = serializers.SerializerMethodField()

    def get_status(self, instance):
        for status in EmployeeStatus:
            if status.name == instance.status:
                return status.value

    def get_rome_status(self, instance):
        for status in RomeStatus:
            if status.name == instance.rome_status:
                return status.value

    class Meta:
        model = Employee
        fields = (
            'first_name', 'last_name', 'job_title', 'telegram', 'photo_url', 'status', 'job_title', 'rome_status'
        )


class EmployeeSerializer(serializers.ModelSerializer):
    manager = SubEmployeeSerializer()

    departament = DepartamentSerializer()
    office = OfficeSerializer()

    status = serializers.SerializerMethodField()
    rome_status = serializers.SerializerMethodField()

    def get_status(self, instance):
        for status in EmployeeStatus:
            if status.name == instance.status:
                return status.value

    def get_rome_status(self, instance):
        for status in RomeStatus:
            if status.name == instance.rome_status:
                return status.value

    class Meta:
        model = Employee
        exclude = ('created_at', 'updated_at')

