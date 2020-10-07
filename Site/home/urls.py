from django.urls import path

from . import views

app_name = 'home'

urlpatterns = [
    path('<int:user_id>/user', views.VacationUser.as_view(), name='user'),
]
