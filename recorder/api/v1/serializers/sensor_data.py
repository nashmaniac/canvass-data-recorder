from rest_framework import serializers


class SensorDataSerializer(serializers.Serializer):
    deviceId = serializers.CharField(required=True, max_length=50)
    timestamp = serializers.DateTimeField(required=True)
    pressure = serializers.FloatField(
        required=False, allow_null=True)
    temperature = serializers.FloatField(
        required=False, allow_null=True)
    status = serializers.CharField(
        max_length=50,
        required=False, default=None, allow_blank=True, allow_null=True)
