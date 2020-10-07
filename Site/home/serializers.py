from rest_framework import serializers


class VacationUserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    is_approver = serializers.BooleanField()
    is_rejector = serializers.BooleanField()
