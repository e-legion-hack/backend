from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from office.models import Office, Departament
from utils.enums import EmployeeStatus, RomeStatus
from utils.models import CreateUpdateTracker, nb


class Employee(CreateUpdateTracker):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    status = models.CharField(
        verbose_name='статус сотрудника',
        max_length=16,
        choices=tuple([(status.name, status.value) for status in EmployeeStatus])
    )
    rome_status = models.CharField(
        verbose_name='римский статус',
        max_length=20,
        choices=tuple([(status.name, status.value) for status in RomeStatus]),
        default=RomeStatus.tubicen.name,
    )

    job_title = models.CharField(
        verbose_name='должность',
        max_length=64,
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
    phone_number = models.PositiveBigIntegerField(default=89661215210)
    email = models.EmailField(default='test@gmail.com')
    about = models.TextField(verbose_name='о себе', **nb)
    photo_url = models.URLField(verbose_name='ссылка на фото', max_length=1024, **nb)

    start_at = models.DateTimeField(verbose_name='начало работы', auto_now_add=True)
    end_at = models.DateTimeField(verbose_name='дата увольнение', **nb)

    is_fired = models.BooleanField(verbose_name='уволен', default=False)

    class Meta(CreateUpdateTracker.Meta):
        abstract = False
        verbose_name = 'сотрудник'
        verbose_name_plural = 'сотрудники'

    def __str__(self):
        return f"{self.first_name} {self.last_name}: {self.job_title}"
