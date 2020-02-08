__author__ = "Jerome Chang"
from django.contrib import admin
from django.urls import path
from sample1 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('login/', views.login),
    path('home/', views.home),
    path('user1/', views.user1),
    path('user2/', views.user2),
]