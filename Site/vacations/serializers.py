from rest_framework import serializers

from Site.home import VacationUserSerializer


class VacationSerializer(serializers.Serializer):
    user = VacationUserSerializer()
    reason = serializers.CharField(source='display_reason')
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    confirmed_by = VacationUserSerializer(allow_null=True)
    confirmed_at = serializers.DateTimeField(allow_null=True)
    rejected_by = VacationUserSerializer(allow_null=True)
    rejection_reason = serializers.CharField(source='display_rejection_reason')
