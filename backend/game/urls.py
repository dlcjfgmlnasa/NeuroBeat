# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path(
        'mini/',
        views.MiniGameView.as_view(),
        name='mini_game get/post'
    ),
    path(
        'mini/<int:pk>/',
        views.MiniGameUpdateDelete.as_view(),
        name='mini_game put/delete'
    )

]
