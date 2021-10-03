from django.urls import path
from .views import TaskAPIView

urlpatterns = [
    path('<int:task_id>/', TaskAPIView.as_view()),
]