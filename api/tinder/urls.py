from django.urls import path
from .views import LikeActivityAPIView

urlpatterns = [
    path('like/', LikeActivityAPIView.as_view())
]