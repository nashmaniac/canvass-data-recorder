from django.urls import include, path

urlpatterns = [
    path('api/', include(('recorder.api.urls', 'recorder'), namespace='api')),
]
