from django.urls import path, include

urlpatterns = [
    path('v1/', include(('recorder.api.v1.urls', 'recorder'), namespace='v1'))
]
