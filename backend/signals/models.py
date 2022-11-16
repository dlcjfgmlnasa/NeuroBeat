# -*- coding:utf-8 -*-
from game.models import Game
from django.db import models
from backend.models import TimeStampedModel


class Device(TimeStampedModel):
    DEVICE_TYPE_CHOICE = (
        (1, 'neurotx_v1'),  # NeuroTx 에서 개발한 첫번째 기기
        (2, 'neurotx_v2')   # 개발 진행 중...
    )
    device_type = models.CharField(
        null=False, blank=False,
        choices=DEVICE_TYPE_CHOICE,
        max_length=5,
        db_column='DEVICE_TYPE'
    )
    sampling_rate = models.FloatField(
        null=False, blank=False,
        db_column='SAMPLING_RATE'
    )

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
    data = models.JSONField(
        db_column='DATA'
    )

    class Meta:
        db_table = 'NG_BIO_SIGNAL'
