# -*- coding:utf-8 -*-
from user.models import User
from django.db import models
from backend.models import TimeStampedModel


class Game(TimeStampedModel):
    RANK_CHOICE = (
        (1, 'S'),
        (2, 'A'),
        (3, 'B'),
        (4, 'C'),
        (5, 'D'),
        (6, 'F'),
    )
    user = models.ForeignKey(
        User, null=True,
        on_delete=models.SET_NULL,
        related_name='game',
        db_column='USER_ID'
    )
    # 뉴로피드백 사용여부
    neuro_feedback = models.BooleanField(
        null=False, blank=False,
        db_column='NEURO_FEEDBACK_FLAG'
    )
    # 바이뉴럴비트 사용여부
    binaural_beats = models.BooleanField(
        null=False, blank=False,
        db_column='BINAURAL_BEATS_FLAG'
    )
    # 게임 속도
    speed = models.FloatField(
        null=False, blank=False,
        db_column='SPEED'
    )
    # 게임 랭크
    rank = models.IntegerField(
        choices=RANK_CHOICE,
        null=False, blank=False,
        db_column='RANK'
    )
    # 총 게임 점수 (= 리듬 게임 / 기억력 게임 / 색상 게임)
    score = models.IntegerField(
        null=False, blank=False,
        db_column='SCORE'
    )
    # 리듬 게임 점수
    rhythm_score = models.IntegerField(
        null=False, blank=False,
        db_column='RHYTHM_SCORE'
    )
    # 기억력 게임 점수
    memory_score = models.IntegerField(
        null=False, blank=False,
        db_column='MEMORY_SCORE'
    )
    # 색상 게임 점수
    color_score = models.IntegerField(
        null=False, blank=False,
        db_column='COLOR_SCORE'
    )

    # -- 리듬 게임 구간에서의 Great/Good/Bad/Miss 개수 -- #
    rhythm_score_great_count = models.IntegerField(
        null=False, blank=False,
        db_column='RHYTHM_SCORE_GREAT_COUNT'
    )
    rhythm_score_good_count = models.IntegerField(
        null=False, blank=False,
        db_column='RHYTHM_SCORE_GOOD_COUNT'
    )
    rhythm_score_bad_count = models.IntegerField(
        null=False, blank=False,
        db_column='RHYTHM_SCORE_BAD_COUNT'
    )
    rhythm_score_miss_count = models.IntegerField(
        null=False, blank=False,
        db_column='RHYTHM_SCORE_MISS_COUNT'
    )

    # -- 기억력 게임 구간에서의 Great/Good/Bad/Miss 개수 -- #
    memory_score_great_count = models.IntegerField(
        null=False, blank=False,
        db_column='MEMORY_SCORE_GREAT_COUNT'
    )
    memory_score_good_count = models.IntegerField(
        null=False, blank=False,
        db_column='MEMORY_SCORE_GOOD_COUNT'
    )
    memory_score_bad_count = models.IntegerField(
        null=False, blank=False,
        db_column='MEMORY_SCORE_BAD_COUNT'
    )
    memory_score_miss_count = models.IntegerField(
        null=False, blank=False,
        db_column='MEMORY_SCORE_MISS_COUNT'
    )

    # -- 색상 맞추기 게임 구간에서의 Great/Good/Bad/Miss 개수 -- #
    color_score_great_count = models.IntegerField(
        null=False, blank=False,
        db_column='COLOR_SCORE_GREAT_COUNT'
    )
    color_score_good_count = models.IntegerField(
        null=False, blank=False,
        db_column='COLOR_SCORE_GOOD_COUNT'
    )
    color_score_bad_count = models.IntegerField(
        null=False, blank=False,
        db_column='COLOR_SCORE_BAD_COUNT'
    )
    color_score_miss_count = models.IntegerField(
        null=False, blank=False,
        db_column='COLOR_SCORE_MISS_COUNT'
    )

    # 최고 콤보 갯수
    max_combo = models.IntegerField(
        null=False, blank=False,
        db_column='MAX_COMBO'
    )
    # 한 게임에서 집중한 정도 (%)
    focused = models.IntegerField(
        null=False, blank=False,
        db_column='FOCUSED'
    )
    # 한 게임 내에서의 평균 집중도
    attention = models.FloatField(
        null=False, blank=False,
        db_column='ATTENTION'
    )

    class Meta:
        db_table = 'NG_GAME'


class MiniGame(TimeStampedModel):
    MINI_GAME_CHOICE = (
        (1, 'Corsi_Block_Test'),
        (2, 'Digit_Span_Test'),
        (3, 'K-TMT-E'),
        (4, 'K-BNT'),
        (5, 'SVLT-E'),
    )
    user = models.ForeignKey(
        User, null=True,
        on_delete=models.SET_NULL,
        related_name='mini_game',
        db_column='USER_ID'
    )
    game_type = models.IntegerField(
        choices=MINI_GAME_CHOICE,
        null=False, blank=False,
        db_column='MINI_GAME_TYPE'
    )
    score = models.IntegerField(
        null=False, blank=False,
        db_column='SCORE'
    )

    class Meta:
        db_table = 'NG_MINI_GAME'
