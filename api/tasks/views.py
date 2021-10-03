from rest_framework.views import APIView

from job.models import Task
from job.serializers import ReadTaskSerializer
from utils.api import CustomJsonResponse


class TaskAPIView(APIView):
    def get(self, request, task_id: int, *args, **kwargs):
        task, errors = Task.get_obj_by_id(task_id)

        return CustomJsonResponse(
            data=ReadTaskSerializer(task).data,
            errors=errors,
        )

