from recorder.models import SensorData
from rest_framework import serializers


class SensorDataInputSerializer(serializers.Serializer):
    deviceId = serializers.CharField(required=True, max_length=50)
    timestamp = serializers.DateTimeField(required=True)
    pressure = serializers.FloatField(
        required=False, allow_null=True)
    temperature = serializers.FloatField(
        required=False, allow_null=True)
    status = serializers.CharField(
        max_length=50,
        required=False, default=None, allow_blank=True, allow_null=True)


class SensorDataSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        request = kwargs.get('context', {}).get('request')
        str_fields = request.GET.get('publisher', '') if request else None
        fields = str_fields.split(',') if str_fields else None

        # Instantiate the superclass normally
        super(SensorDataSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = SensorData
        fields = '__all__'
