from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel


class SensorDataStatus(models.TextChoices):
    ON = 'on', _('ON')
    OFF = 'off', _('OFF')
    ACTIVE = 'active', _('ACTIVE')
    INACTIVE = 'inactive', _('INACTIVE')
    __empty__ = _('UNKNOWN')


class Sensor(TimeStampedModel):
    id = models.CharField(max_length=20, primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=True,
                            blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'sensors'


# Create your models here.
class SensorData(TimeStampedModel):

    device = models.ForeignKey(
        Sensor, related_name='sendor_data', on_delete=models.CASCADE)
    record_time = models.DateTimeField()
    status = models.CharField(
        max_length=50,
        choices=SensorDataStatus.choices,
        default=SensorDataStatus.__empty__
    )
    pressure = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'sensor_data'
        ordering = ('-record_time',)
