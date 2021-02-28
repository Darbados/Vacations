from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
    path('employee/<int:pk>/details/json', views.EmployeeInfo.as_view(), name='employee_json'),
]
