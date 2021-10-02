from __future__ import annotations

import uuid
from typing import Optional, Union, Tuple, Dict

from django.db import models


nb = dict(null=True, blank=True)


class CreateTracker(models.Model):
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

    @classmethod
    def get_obj_by_id(
            cls,
            instance_id: Optional[Union[str, int, uuid.uuid4]] = None,
            **kwargs
    ) -> Tuple[Optional['cls'], Optional[Dict[str, str]]]:
        """
        returns instance, None if there is an objects with given id.
        Or None, dict with error's text
        """
        try:
            if instance_id is not None:
                instance = cls.objects.get(pk=instance_id)
            else:
                instance = cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            return None, {"error": f"{cls.__name__} object with id={instance_id} doesn't exist."}
        else:
            return instance, None


class CreateUpdateTracker(CreateTracker):
    updated_at = models.DateTimeField(verbose_name='дата обновления', auto_now=True)

    class Meta(CreateTracker.Meta):
        abstract = True
