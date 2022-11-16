# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path(
        'main/',
        views.MainGameView.as_view(),
        name='game get/post'
    ),
    path(
        'main/<int:pk>/',
        views.MainGameDetailView.as_view(),
        name='main put/delete'
    ),
    path(
        'mini/',
        views.MiniGameView.as_view(),
        name='mini_game get/post'
    ),
    path(
        'mini/<int:pk>/',
        views.MiniGameDetailView.as_view(),
        name='mini_game put/delete'
    )
]
