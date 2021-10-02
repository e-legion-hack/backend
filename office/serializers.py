from rest_framework import serializers

from office.models import Departament, Office
from utils.enums import Department, City


class OfficeSerializer(serializers.ModelSerializer):
    city = serializers.SerializerMethodField()

    def get_city(self, instance):
        for city in City:
            if city.name == instance.city:
                return city.value

    class Meta:
        model = Office
        exclude = ('created_at', 'id')


class DepartamentSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, instance):
        for dep in Department:
            if dep.name == instance.name:
                return dep.value

    class Meta:
        model = Departament
        exclude = ('created_at', 'id')
