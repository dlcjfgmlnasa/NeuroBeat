# -*- coding:utf-8 -*-
from game.models import Game
from django.db import models
from backend.models import TimeStampedModel


class Device(TimeStampedModel):
    DEVICE_TYPE_CHOICE = (
        (1, 'neurotx_v1'),  # NeuroTx 에서 개발한 첫번째 기기
        (2, 'neurotx_v2')   # 개발 진행 중인 기기... 추후에 추가될 수 있음
    )
    device_type = models.IntegerField(
        null=False, blank=False,
        choices=DEVICE_TYPE_CHOICE,
        db_column='DEVICE_TYPE'
    )
    sampling_rate = models.FloatField(
        null=False, blank=False,
        db_column='SAMPLING_RATE'
    )
    description = models.TextField(
        null=True, blank=True,
        max_length=100,
        db_column='DESCRIPTION'
    )

    def __str__(self):
        return '{}'.format(self.get_device_type_display())

    class Meta:
        db_table = 'NG_DEVICE'


class BioSignal(TimeStampedModel):
    game = models.ForeignKey(
        Game, null=True,
        on_delete=models.SET_NULL,
        related_name='bio_signal',
        db_column='GAME_ID'
    )
    device = models.ForeignKey(
        Device, null=True,
        on_delete=models.SET_NULL,
        related_name='bio_signal',
        db_column='DEVICE_ID'
    )
    sample_size = models.IntegerField(
        null=False, blank=False,
        db_column='SAMPLE_SIZE'
    )
    data = models.JSONField(
        null=False, blank=False,
        db_column='DATA'
    )

    class Meta:
        db_table = 'NG_BIO_SIGNAL'
