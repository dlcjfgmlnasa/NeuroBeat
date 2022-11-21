# -*- coding:utf-8 -*-
from django.contrib import admin
from signals.models import Device, BioSignal


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'device_type',
        'sampling_rate',
        'description',
        'int_dt',
        'upt_dt'
    )


@admin.register(BioSignal)
class BioSignalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'game',
        'device',
        'sample_size'
    )