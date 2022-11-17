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


class BioSignalSerializer(serializers.ModelSerializer):
    data = serializers.JSONField(write_only=True)
    sample_size = serializers.IntegerField(read_only=True)

    class Meta:
        model = BioSignal
        fields = (
            'id',
            'game',
            'device',
            'sample_size',
            'data'
        )
