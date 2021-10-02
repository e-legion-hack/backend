from django.db import models

# Create your models here.
from employee.models import Employee
from utils.enums import TaskStatus
from utils.models import CreateUpdateTracker, nb


class Task(CreateUpdateTracker):
    """
        It might be one time task. For example, fix monitor or keyboard issue for backoffice.
        Or part of big project.
    """
    status = models.CharField(
        verbose_name='статус', max_length=16, choices=tuple([(status.name, status.value) for status in TaskStatus])
    )

    title = models.CharField(verbose_name='Заголовок', max_length=64)

    creator = models.ForeignKey(Employee, verbose_name='создатель', on_delete=models.PROTECT)
    executors = models.ManyToManyField(Employee, verbose_name='исполнители')

    commentary = models.TextField(verbose_name='подробное описание', **nb)

    finished_at = models.DateTimeField(verbose_name='время окончания', **nb)


class Project(CreateUpdateTracker):
    """Big project. It might be contained from a lot of tasks"""
    name = models.CharField(
        verbose_name='название проекта', max_length=64, help_text='Например, "разработка приложения для Burger King".'
    )
