# -*- coding:utf-8 -*-
from django.db import models
from backend.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, TimeStampedModel):
    GENDER_CHOICE = (
        (0, 'None'),
        (1, 'MALE'),
        (2, 'FEMALE'),
    )
    # 성별
    gender = models.CharField(
        choices=GENDER_CHOICE,
        max_length=20,
        null=False, blank=False,
        db_column='GENDER'
    )
    # 생년 월일
    birth = models.DateField(
        max_length=25,
        null=True, blank=True,
        db_column='BIRTH'
    )
    # 병명
    diagnosis = models.CharField(
        max_length=100,
        null=True, blank=True,
        db_column='DIAGNOSIS'
    )
    # 집중도
    attention = models.FloatField(
        null=True, blank=True,
        db_column='ATTENTION'
    )
    first_name = None
    last_name = None

    class Meta:
        db_table = 'NG_USER'
        ordering = ['pk']
