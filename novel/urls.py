__author__ = "Jerome"
from django.contrib import admin
from django.urls import path, include
from novel import views

urlpatterns = [
    path('home/', views.home),
    path('chapter/<int:a_id>.html', views.chapter),
    path('chapter/<int:a_id>/<int:c_id>.html', views.chapter),
    path('category/<int:a_id>.html', views.category),
    path('search/', views.search),
    path('art/getBookText/', views.get_book_text),
    path('', views.home),
]
