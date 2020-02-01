__author__ = "Jerome Chang"

from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('sign-in/', views.sign_in),
    path('record/', views.record),
    path('detail/', views.detail),
]