from django.urls import path
from . import views
from django.shortcuts import render

urlpatterns = [
    path('', views.login, name='login_page'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]
