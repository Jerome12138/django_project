__author__ = "Jerome"
from django.contrib import admin
from django.urls import path, include
from video import views
from video import admin_views

adminpatterns = [
    path('del_request/', admin_views.del_request),
    path('add_vod/', admin_views.add_vod),
    path('view_log/<str:log_date>/', admin_views.view_log),
    path('view_log/', admin_views.view_log),
    path('update_log/', admin_views.update_log),
    path('access_log/', admin_views.access_log),
    path('error_log/', admin_views.error_log),
    path('update_video/', admin_views.update_video),
    path('update/', admin_views.update),
    path('update2/', admin_views.update2),
    path('get_request/', admin_views.get_request),
    path('get_carousel/', admin_views.get_carousel),
    path('add_carousel/', admin_views.carousel_add),
    path('del_carousel/', admin_views.carousel_del),

    # 其他
    path('url2_clear/', admin_views.url2_clear),
    path('url_clear/', admin_views.url_clear),
    path('test/', admin_views.test),
]

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
    path('admin/', include(adminpatterns)),
    path('', views.home),
]
