from django.db import transaction
from django.db.models import ExpressionWrapper, IntegerField, QuerySet
from django.db.models.functions import ExtractMinute, TruncMinute
from django_pandas.io import read_frame
import pandas as pd
from datetime import datetime
from ..models import *


class SensorDataLayer:
    @classmethod
    def get_sensor_data_for_sensor(cls, sensor_id: str) -> QuerySet:
        return SensorData.objects.filter(
            device_id=sensor_id
        ).all()

    @classmethod
    def get_histogram_data(cls, sensor_id: str, diff: int):
        minute_expression = ExpressionWrapper(
           ExtractMinute('record_time') % diff, output_field=IntegerField(),
        )
        queryset = cls.get_sensor_data_for_sensor(sensor_id=sensor_id)
        queryset = queryset.annotate(
            min_to_deduct=minute_expression,
            time_in_minute=TruncMinute('record_time'),
        )
        field_names = ['device_id', 'record_time', 'temperature', 'pressure', 'status', 'min_to_deduct', 'time_in_minute']
        df = read_frame(queryset, fieldnames=field_names)
        df['deltas'] = pd.to_timedelta(df['min_to_deduct'],unit='m')
        df['bin_time'] = (df['time_in_minute'] - df['deltas']).dt.strftime('%Y-%m-%d %H:%M %p')
        data = df.groupby('bin_time')['status'].value_counts().unstack().fillna(0).reset_index().to_dict(orient='records')
        return data

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
