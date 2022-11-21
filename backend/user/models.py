# -*- coding:utf-8 -*-
from django.db import models
from backend.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser, TimeStampedModel):
    GENDER_CHOICE = (
        (1, 'MALE'),
        (2, 'FEMALE'),
    )
    # 성별
    gender = models.IntegerField(
        choices=GENDER_CHOICE,
        null=True, blank=True,
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

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'NG_USER'
        ordering = ['pk']


