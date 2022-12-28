# -*- coding:utf-8 -*-
import json
import numpy as np
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from game.models import Game
from signals.serializer import DeviceSerializers, BioSignalSerializer
from signals.models import Device
from signals.algorithms import attention
from django.contrib.auth import get_user_model


USER_MODEL = get_user_model()


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
    @staticmethod
    def get_parameter(request):
        game_pk = request.GET.get('game_id')
        device_pk = request.GET.get('device_id')
        return game_pk, device_pk

    def post(self, request):
        game_pk, device_pk = self.get_parameter(request)
        if game_pk is None or device_pk is None:
            return Response(
                {
                    'error': '파라미터에 game_pk 그리고 device_pk 을 입력하시오'
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            game = Game.objects.get(id=game_pk)
        except Game.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        try:
            device = Device.objects.get(id=device_pk)
        except Device.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        serializer_cls = BioSignalSerializer(data=request.data)
        if serializer_cls.is_valid():
            serializer_cls.save(
                game=game,
                device=device,
                sample_size=len(json.loads(request.data['data'])['Time'])
            )
            return Response(
                serializer_cls.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer_cls.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class EstimateAttentionAPIView(APIView):
    def post(self, request, device_pk):
        try:
            device = Device.objects.get(id=device_pk)
        except Device.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            user = get_user_model().objects.get(
                id=request.auth.payload['user_id']
            )
        except USER_MODEL.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        data = request.POST.get('data')
        if data is None:
            result = {'error': '[data]를 입력하세요.'}
            return Response(
                result,
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            data = json.loads(data)
            eeg1, eeg2 = data['EEG1'], data['EEG2']
            eeg = np.stack([list(eeg1.values()), list(eeg2.values())], axis=0)
        except KeyError:
            return Response(
                {'error': '입력값의 형태가 옳바르지 않습니다.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        eeg = eeg[~np.isnan(eeg)]
        eeg = eeg.T
        attention_value = attention(data=eeg, sfreq=device.sampling_rate)
        result = {'attention_value': str(attention_value), 'baseline_attention': str(user.attention)}
        return Response(
            result,
            status=status.HTTP_200_OK
        )
