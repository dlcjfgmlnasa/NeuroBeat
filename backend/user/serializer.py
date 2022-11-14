# -*- coding:utf-8 -*-
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


USER_MODEL = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['name'] = user.username
        token['is_staff'] = user.is_staff

        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = USER_MODEL
        fields = (
            'pk',
            'username',
            'gender',
            'birth',
            'diagnosis',
            'attention'
        )
        read_only_fields = (
            'pk',
            'username',
        )


class AccountCreateSerializer(serializers.ModelSerializer):
    birth = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = USER_MODEL
        fields = (
            'pk',
            'password',
            'username',
            'gender',
            'birth',
            'diagnosis',
            'attention'
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5,
            }
        }

    def create(self, validated_data):
        password = validated_data['password']
        del validated_data['password']
        user = USER_MODEL.objects.create(**validated_data)

        user.set_password(password)
        user.save()
        return user
