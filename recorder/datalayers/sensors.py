from ..models import *
from django.db import transaction


class SensorDataLayer:
    @classmethod
    def record_sensor_data(cls, data: dict) -> SensorData:
        with transaction.atomic():
            # create sensor first
            sensor, created = Sensor.objects.get_or_create(
                name=data["deviceId"],
                id=data["deviceId"],
            )
            # create sensor data in db
            sensor_data = SensorData(
                device=sensor,
                record_time=data["timestamp"],
                status=data["status"],
                pressure=data["pressure"],
                temperature=data["temperature"]
            )
            sensor_data.save()
            return sensor_data
        return None
