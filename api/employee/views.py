from rest_framework.request import Request
from rest_framework.views import APIView

from employee.models import Employee
from employee.serializers import EmployeeSerializer
from utils.api import CustomJsonResponse


class EmployeeAPIView(APIView):
    def get(self, request: Request, employee_id: int, *args, **kwargs):
        employee, errors = Employee.get_obj_by_id(instance_id=employee_id)

        return CustomJsonResponse(
            data=EmployeeSerializer(employee).data,
            errors=errors,
        )
