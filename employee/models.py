from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from office.models import Office, Departament
from utils.enums import EmployeeStatus
from utils.models import CreateUpdateTracker, nb


class Employee(CreateUpdateTracker, AbstractUser):
    status = models.CharField(
        verbose_name='статус сотрудника',
        max_length=16,
        choices=tuple([(status.name, status.value) for status in EmployeeStatus])
    )
    job_title = models.CharField(
        verbose_name='должность',
        max_length=16,

    )

    manager = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Начальник', related_name='sub', **nb)

    is_teamlead = models.BooleanField(verbose_name='Тимлид', default=False)
    is_head_of_departament = models.BooleanField(verbose_name='Руководитель отдела', default=False)

    departament = models.ForeignKey(Departament, verbose_name='Департамент', on_delete=models.PROTECT)
    office = models.ForeignKey(Office, verbose_name='офис', on_delete=models.PROTECT)

    is_remote = models.BooleanField(verbose_name='удаленный сотрудник', default=False)

    telegram = models.CharField(max_length=64, **nb)
    instagram = models.CharField(max_length=64, **nb)
    vkontakte = models.CharField(max_length=64, **nb)
    about = models.TextField(verbose_name='о себе', **nb)
    photo_url = models.URLField(verbose_name='ссылка на фото', max_length=1024, **nb)

    start_at = models.DateTimeField(verbose_name='начало работы', auto_now_add=True)
    end_at = models.DateTimeField(verbose_name='дата увольнение', **nb)

    is_fired = models.BooleanField(verbose_name='уволен', default=False)

    class Meta(CreateUpdateTracker.Meta):
        abstract = False
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'
