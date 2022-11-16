# -*- coding:utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from game.models import MiniGame, Game
from game.serializer import MiniGameSerializer, MainGameSerializer
from rest_framework.response import Response

USER_MODEL = get_user_model()


class MainGameView(APIView):
    @staticmethod
    def get_user(request):
        try:
            user = get_user_model().objects.get(
                id=request.auth.payload['user_id']
            )
            return user
        except USER_MODEL.DoesNotExist:
            return None

    def get(self, request):
        user = self.get_user(request)
        game = Game.objects.filter(user=user)
        serializer_cls = MainGameSerializer(game, many=True)

        return Response(
            serializer_cls.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        user = self.get_user(request)
        if user is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_cls = MainGameSerializer(data=request.data)
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


class MainGameDetailView(APIView):
    @staticmethod
    def get_game(pk):
        try:
            game = Game.objects.get(pk=pk)
            return game
        except Game.DoesNotExist:
            return None

    def put(self, request, pk):
        game = self.get_game(pk)
        if game is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = MainGameSerializer(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(
            serializer.errors,
            status=status.HTTP_200_OK
        )

    def delete(self, request, pk):
        game = self.get_game(pk)
        if game is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        game.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class MiniGameView(APIView):
    @staticmethod
    def get_user(request):
        try:
            user = get_user_model().objects.get(
                id=request.auth.payload['user_id']
            )
            return user
        except USER_MODEL.DoesNotExist:
            return None

    def get(self, request):
        user = self.get_user(request)
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

    def post(self, request):
        user = self.get_user(request)
        if user is None:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_cls = MiniGameSerializer(data=request.data)
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


class MiniGameDetailView(APIView):
    @staticmethod
    def get_mini_game(pk):
        try:
            mini_game = MiniGame.objects.get(pk=pk)
            return mini_game
        except MiniGame.DoesNotExist:
            return None

    def put(self, request, pk):
        mini_game = self.get_mini_game(pk)
        serializer_cls = MiniGameSerializer(mini_game, data=request.data)
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

    def delete(self, request, pk):
        mini_game = self.get_mini_game(pk)
        mini_game.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
