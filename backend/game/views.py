# -*- coding:utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from game.models import MiniGame, Game
from game.serializer import MiniGameSerializer
from rest_framework.response import Response

USER_MODEL = get_user_model()


class MiniGameView(APIView):
    @staticmethod
    def get_user(requests):
        try:
            user = get_user_model().objects.get(
                id=requests.auth.payload['user_id']
            )
            return user
        except USER_MODEL.DoesNotExist:
            return None

    def get(self, requests):
        user = self.get_user(requests)
        if user is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        mini_game = MiniGame.objects.filter(user=user)
        serializer_cls = MiniGameSerializer(mini_game, many=True)
        return Response(
            serializer_cls.data,
            status=status.HTTP_200_OK
        )

    def post(self, requests):
        user = self.get_user(requests)
        if user is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_cls = MiniGameSerializer(data=requests.data)
        if serializer_cls.is_valid():
            serializer_cls.save(user=user)
            return Response(
                serializer_cls.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer_cls.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class MiniGameUpdateDelete(APIView):
    @staticmethod
    def get_mini_game(pk):
        try:
            mini_game = MiniGame.objects.get(pk=pk)
            return mini_game
        except MiniGame.DoesNotExist:
            return None

    def put(self, requests, pk):
        mini_game = self.get_mini_game(pk)
        serializer_cls = MiniGameSerializer(mini_game, data=requests.data)
        if serializer_cls.is_valid():
            serializer_cls.save()
            return Response(
                serializer_cls.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer_cls.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, requests, pk):
        mini_game = self.get_mini_game(pk)
        mini_game.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
