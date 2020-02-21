__author__ = "Jerome"
from django.contrib import admin
from django.urls import path, include
from video import views
adminpatterns = [
    path('del_request/', views.del_request),
    path('add_vod/', views.add_vod),
    path('view_log/<str:log_date>/', views.view_log),
    path('view_log/', views.view_log),
    path('update/', views.update),
    # path('update_list/',views.update_list),
    path('', views.admin),
]

urlpatterns = [
    path('home/', views.home),
    path('play/<str:vod_id>/', views.play),
    path('play/<str:vod_id>/<int:index>/', views.play),
    path('play2/', views.play2),
    path('search/', views.search),
    path('search2/', views.search2),
    path('type/<str:vod_cid>/', views.vod_type),
    path('push_request/', views.push_request),
    path('admin/', include(adminpatterns)),
    path('', views.home),
]
