# -*- coding:utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.UserView.as_view(),
        name='user'
    ),
    path(
        'list/',
        views.UserListView.as_view(),
        name='user list'
    ),
    path(
        'account/',
        views.AccountView.as_view(),
        name='account'
    )
]