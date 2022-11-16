# -*- coding:utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from signals.serializer import DeviceSerializers
from signals.models import Device, BioSignal


class DeviceAPIView(APIView):
    def post(self, request):
        serializer_cls = DeviceSerializers(data=request.data)
        if serializer_cls.is_valid():
            serializer_cls.save()
            return Response(
                serializer_cls.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer_cls.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DeviceDetailAPIView(APIView):
    @staticmethod
    def get_device(pk):
        try:
            device = Device.objects.get(pk=pk)
            return device
        except Device.DoesNotExist:
            return None

    def put(self, request, pk):
        device = self.get_device(pk)
        if device is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_cls = DeviceSerializers(device, data=request.data)
        if serializer_cls.is_valid():
            serializer_cls.save()
            return Response(
                serializer_cls.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer_cls.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        device = self.get_device(pk)
        if device is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        device.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class BioSignalAPIView(APIView):
    def post(self, request):
        return Response(
            status=status.HTTP_200_OK
        )


class EstimateAttentionAPIView(APIView):
    def post(self, requests):
        return Response(
            status=status.HTTP_200_OK
        )