from django.db import models


nb = dict(null=True, blank=True)


class CreateTracker(models.Model):
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class CreateUpdateTracker(CreateTracker):
    updated_at = models.DateTimeField(verbose_name='дата обновления', auto_now=True)

    class Meta(CreateTracker.Meta):
        abstract = True
