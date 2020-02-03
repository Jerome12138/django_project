__author__ = "Jerome Chang"
from django.contrib import admin
from django.urls import path
from video import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', views.home),
    path('play/', views.play),
    path('play2/<int:index>/', views.play2),
    path('',views.home),
]