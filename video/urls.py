__author__ = "Jerome"
from django.contrib import admin
from django.urls import path, include
from video import views


urlpatterns = [
    path('home/', views.home),
    path('type/<str:vod_cid>/', views.vod_type),
    path('play/<str:vod_id>/', views.play),
    path('play/<str:vod_id>/<int:url_index>-<int:index>.html', views.play),
    path('play2/', views.play2),
    path('i-search/', views.i_search),
    path('i-play/', views.i_play),
    path('jx-play/', views.jx_play),
    path('search/', views.search),
    path('search2/', views.search2),
    path('push_request/', views.push_request),
    path('', views.home),
]
