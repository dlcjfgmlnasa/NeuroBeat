# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.BioSignalAPIView.as_view(),
        name='bio_signal'
    ),
    path(
        'attention_estimation/',
        views.EstimateAttentionAPIView.as_view(),
        name='attention estimation'
    ),
    path(
        'device/',
        views.DeviceAPIView.as_view(),
        name='device post'
    ),
    path(
        'device/<int:pk>/',
        views.DeviceDetailAPIView.as_view(),
        name='device put/delete'
    )
]