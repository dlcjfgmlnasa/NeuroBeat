# -*- coding:utf-8 -*-
from rest_framework import serializers
from user.serializer import UserSerializer
from game.models import Game, MiniGame


class MiniGameSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = MiniGame
        fields = '__all__'
