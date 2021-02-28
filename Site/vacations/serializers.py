from rest_framework import serializers

from home.serializers import EmployeeSerializer


class DescriptionSerializer(serializers.Serializer):
    description = serializers.CharField()


class VacationSerializer(serializers.Serializer):
    user = EmployeeSerializer()
    reason = DescriptionSerializer()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    confirmed_by = EmployeeSerializer(allow_null=True)
    confirmed_at = serializers.DateTimeField(allow_null=True)
    rejected_by = EmployeeSerializer(allow_null=True)
    rejection_reason = DescriptionSerializer()
