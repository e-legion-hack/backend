from django.urls import path
from .views import LikeActivityAPIView, CreateActivityAPIView

urlpatterns = [
    path('like/', LikeActivityAPIView.as_view()),
    path('', CreateActivityAPIView.as_view()),
]