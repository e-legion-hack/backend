from rest_framework.request import Request
from rest_framework.views import APIView

from api.employee.utils import get_activities_for_employee
from employee.models import Employee
from employee.serializers import EmployeeSerializer
from tinder.models import Activity
from utils.api import CustomJsonResponse


class EmployeeAPIView(APIView):
    def get(self, request: Request, employee_id: int, *args, **kwargs):
        employee, errors = Employee.get_obj_by_id(instance_id=employee_id)

        return CustomJsonResponse(
            data=EmployeeSerializer(employee).data,
            errors=errors,
        )


class EmployeeTinderAPIView(APIView):
    def get(self, request: Request, employee_id: int, *args, **kwargs):
        employee_activities, other_employee_activities = get_activities_for_employee(employee_id)

        return CustomJsonResponse(
            data={
                'employee': employee_activities,
                'other': other_employee_activities,
            },
            errors=None,
        )


class DeleteActivityAPIView(APIView):
    def post(self, request: Request, employee_id: int, activity_id, *args, **kwargs):
        res = Activity.objects.filter(creator_id=employee_id, id=activity_id).delete()

        return CustomJsonResponse(
            data={
                'res': f"Deleted {res} rows"
            },
            errors=None
        )
