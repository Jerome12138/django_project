__author__ = "Jerome Chang"
from django.contrib import admin
from django.urls import path
from video import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('home/', views.home),
    path('play/<str:vod_id>/', views.play),
    path('play/<str:vod_id>/<int:index>/', views.play),
    path('play2/', views.play2),
    path('search/',views.search),
    path('type/<str:vod_cid>/',views.vod_type),
    path('push_request/',views.push_request),
    path('admin/',views.admin),
    path('admin/del_request/',views.del_request),
    path('admin/add_vod/',views.add_vod),
    path('admin/view_log/<str:log_date>/',views.view_log),
    path('admin/view_log/',views.view_log),
    path('admin/test/',views.get_resources),
    # path('admin/update_list/',views.update_list),
    path('',views.home),
]