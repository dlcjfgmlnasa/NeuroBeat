# -*- coding:utf-8 -*-
from signals.models import Device, BioSignal
from rest_framework import serializers
from game.serializer import MainGameSerializer


class DeviceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = (
            'id',
            'device_type',
            'sampling_rate',
            'description'
        )


class BioSignalInputSerializer(serializers.ModelSerializer):
    game = MainGameSerializer(read_only=True)
    device = DeviceSerializers(read_only=True)

    class Meta:
        model = BioSignal
        write_only_fields = (
            'data'
        )
        fields = (
            'game',
            'device',
            'data'
        )
