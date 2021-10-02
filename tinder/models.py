from django.db import models

from employee.models import Employee
from utils.enums import ActivityType
from utils.models import CreateTracker, nb


class Activity(CreateTracker):
    creator = models.ForeignKey(Employee, on_delete=models.PROTECT, verbose_name='создатель заявки')

    name = models.CharField(max_length=64)
    category = models.CharField(
        max_length=16,
        verbose_name='заголовок',
        choices=tuple(
            [(activity.name, activity.value) for activity in ActivityType]
        )
    )

    photo_url = models.URLField(max_length=1024, verbose_name='ссылка на фото', **nb)

    place = models.CharField(max_length=32, verbose_name='место встречи')

    dttm = models.DateTimeField(verbose_name='время мероприятия')

    class Meta(CreateTracker.Meta):
        abstract = False
        verbose_name = 'активность'
        verbose_name_plural = 'активности'


class LikedActivity(CreateTracker):
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        f"{self.employee_id} liked {self.activity_id}"
