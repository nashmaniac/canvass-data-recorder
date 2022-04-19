from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SensorDataHealthApiView(APIView):
    def get(self, request):
        return Response(
            data=dict(
                status='200',
                message='Up and running',
            ),
            status=status.HTTP_200_OK
        )
