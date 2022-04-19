from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import SensorDataSerializer


class SensorDataHealthApiView(APIView):
    def get(self, request):
        return Response(
            data=dict(
                status='200',
                message='Up and running',
            ),
            status=status.HTTP_200_OK
        )


class SensorDataApiView(APIView):
    serializer_class = SensorDataSerializer

    def post(self, request):
        serializer_class = self.serializer_class
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(
            serializer.validated_data, status=status.HTTP_200_OK
        )
