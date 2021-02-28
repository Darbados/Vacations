from django.contrib import messages
from django.http import HttpResponse
from rest_framework.generics import RetrieveAPIView

from home.models import Employee
from home.serializers import EmployeeSerializer


def index(request):
    messages.info(request, 'Index view')
    return HttpResponse('Hello Vacations app')


class EmployeeInfo(RetrieveAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.filter(deactivated_at__isnull=True)
