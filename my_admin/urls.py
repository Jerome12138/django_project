__author__ = "Jerome"

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login.html', views.SignIn.as_view()),
    path('register.html', views.SignUp.as_view()),
    path('logout.html', views.log_out),
    path('upload/', views.upload),
    path('', views.admin)
]
