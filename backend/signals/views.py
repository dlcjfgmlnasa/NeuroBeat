# -*- coding:utf-8 -*-
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from signals.algorithms import attention


class EstimateAttention(APIView):
    def post(self, requests):
        return Response(
            status=status.HTTP_200_OK
        )