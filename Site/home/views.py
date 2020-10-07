from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from home.models import VacationsUser
from home.serializers import VacationUserSerializer


class VacationUser(APIView):
    def get(self, request, user_id):
        return Response(VacationUserSerializer(VacationsUser.objects.get(pk=user_id)).data)

