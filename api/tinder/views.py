from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status

from tinder.serializers import ActivityLikedSerializer
from utils.api import CustomJsonResponse


class LikeActivityAPIView(APIView):
    def post(self, request: Request, *args, **kwargs):
        data = request.data
        activity = data.get('activity')
        employee = data.get('employee')

        activity_liked, errors = ActivityLikedSerializer.save_data(data)

        return CustomJsonResponse(
            data=ActivityLikedSerializer(activity_liked).data,
            errors=errors,
            success_code=status.HTTP_201_CREATED,
            error_code=status.HTTP_400_BAD_REQUEST,
        )