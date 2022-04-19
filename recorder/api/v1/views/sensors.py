from recorder.api.v1.serializers.sensor_data import (SensorDataInputSerializer,
                                                     SensorDataSerializer)
from recorder.datalayers import SensorDataLayer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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
    serializer_class = SensorDataInputSerializer

    def post(self, request):
        serializer_class = self.serializer_class
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        sensor_data = SensorDataLayer.record_sensor_data(
            serializer.validated_data)
        return Response(
            SensorDataSerializer(sensor_data).data, status=status.HTTP_200_OK
        )


class SensorHistogramApiView(APIView):
    def get(self, request):
        sensor_id = request.query_params.get('sensor')
        diff = request.query_params.get('diff', 30)
        sensor_data = SensorDataLayer.get_histogram_data(
            sensor_id=sensor_id, diff=diff)
        return Response(
            data=dict(
                data=sensor_data
            ),
            status=status.HTTP_200_OK
        )
