from datetime import datetime
from django.db.models import Subquery
from typing import Tuple, Dict

from tinder.models import Activity, LikedActivity
from tinder.serializers import BaseActivitySerializer


def get_activities_for_employee(employee_id: int) -> Tuple[Dict, Dict]:
    created_activities = Activity.objects.filter(
        creator_id=employee_id, dttm__gt=datetime.now()
    )

    liked_by_employee = LikedActivity.objects.filter(employee_id=employee_id)
    created_by_other_activities = Activity.objects.exclude(
        creator_id=employee_id,
    ).filter(
        dttm__gt=datetime.now()
    ).exclude(
        # exclude those which has been liked by this employee
        pk__in=Subquery(liked_by_employee.values('activity_id'))
    )

    return (
        BaseActivitySerializer(created_activities, many=True).data,
        BaseActivitySerializer(created_by_other_activities, many=True).data
    )
