from django.urls import path, include
from .views import *

sensor_data_urlpatterns = [
    path('', SensorDataApiView.as_view(), name='sensor_data_api_view'),
    path('histogram', SensorHistogramApiView.as_view(), name='sensor_histogram_api_view'),
]

urlpatterns = [
    path('healthz', SensorDataHealthApiView.as_view(), name='health_api_view'),
    path('sensor-data/', include(sensor_data_urlpatterns)),
]
