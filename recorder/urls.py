from django.urls import path, include

urlpatterns = [
    path('api/', include(('recorder.api.urls', 'recorder'), namespace='api'))
]
