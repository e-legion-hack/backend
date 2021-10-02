from django.db import models

# Create your models here.
from utils.enums import City, Department
from utils.models import CreateTracker


class Office(CreateTracker):
    city = models.CharField(
        verbose_name='город', max_length=8, choices=tuple([(city.name, city.value) for city in City])
    )
    name = models.CharField(verbose_name='название', max_length=64)
    address = models.CharField(verbose_name='адрес', max_length=128)
    phone = models.PositiveBigIntegerField(verbose_name='контактный номер')
    email = models.EmailField()

    class Meta(CreateTracker.Meta):
        abstract = False
        verbose_name = 'офис'
        verbose_name_plural = 'офисы'

    def __str__(self):
        return f"{self.city}"


class Departament(CreateTracker):
    name = models.CharField(max_length=32, choices=tuple([(dep.name, dep.value) for dep in Department]))

    class Meta(CreateTracker.Meta):
        abstract = False
        verbose_name = 'отдел'
        verbose_name_plural = 'отделы'

    def __str__(self):
        return f"{self.name}"
