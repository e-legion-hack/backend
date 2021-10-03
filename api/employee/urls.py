from django.urls import path
from .views import EmployeeAPIView, EmployeeTinderAPIView, DeleteActivityAPIView

urlpatterns = [
    # GET employee by id
    path('<int:employee_id>/', EmployeeAPIView.as_view()),

    # GET activities created by mine and by others
    path('<int:employee_id>/e-tinder/', EmployeeTinderAPIView.as_view()),

    # POST delete activity created by me
    path('<int:employee_id>/e-tinder/<int:activity_id>/delete/', DeleteActivityAPIView.as_view()),
]