from django.urls import path
from .views import *
urlpatterns = [
    path('healthz', SensorDataHealthApiView.as_view(), name='health_api_view'),
]
