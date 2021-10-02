from django.urls import path
from .views import EmployeeAPIView, EmployeeTinderAPIView

urlpatterns = [
    path('<int:employee_id>/', EmployeeAPIView.as_view()),
    path('<int:employee_id>/e-tinder/', EmployeeTinderAPIView.as_view()),
]