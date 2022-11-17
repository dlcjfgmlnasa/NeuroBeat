# -*- coding:utf-8 -*-
from django.contrib import admin
from game.models import Game, MiniGame


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'score',
        'rhythm_score',
        'memory_score',
        'color_score',
        'int_dt',
        'upt_dt'
    )


@admin.register(MiniGame)
class MiniGameAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'game_type',
        'score',
        'int_dt',
        'upt_dt'
    )

