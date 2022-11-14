# -*- coding:utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from user.serializer import AccountCreateSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from user.serializer import UserSerializer
from .serializer import MyTokenObtainPairSerializer


USER_MODEL = get_user_model()


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserView(APIView):
    def get(self, request):
        try:
            user = get_user_model().objects.get(
                id=request.auth.payload['user_id']
            )
        except USER_MODEL.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )

        serializer_cls = UserSerializer(user)
        return Response(
            serializer_cls.data,
            status=status.HTTP_200_OK
        )

    def put(self, request):
        try:
            user = get_user_model().objects.get(
                id=request.auth.payload['user_id']
            )
        except USER_MODEL.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        serializer_cls = UserSerializer(user, data=request.data)
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

    def delete(self, request):
        try:
            user = get_user_model().objects.get(
                id=request.auth.payload['user_id']
            )
        except USER_MODEL.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND
            )
        user.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )


class UserListView(APIView):
    def get(self, request):
        users = get_user_model().objects.all()
        serializer_cls = UserSerializer(users, many=True)
        return Response(
            serializer_cls.data,
            status=status.HTTP_200_OK,
        )


class AccountView(APIView):
    permission_classes = [AllowAny]

    # 회원 가입
    def post(self, request):
        serializer_cls = AccountCreateSerializer(data=request.data)
        if serializer_cls.is_valid():
            serializer_cls.save()

            return Response(
                serializer_cls.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer_cls.errors,
            status=status.HTTP_404_NOT_FOUND
        )

