__author__ = "Jerome"
from django.contrib import admin
from django.urls import path, include
from novel import views

urlpatterns = [
    path('home/', views.home),
    path('chapter/', views.chapter),
    path('', views.home),
]
