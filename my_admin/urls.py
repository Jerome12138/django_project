__author__ = "Jerome"

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # 登录注册
    path('login.html', views.SignIn.as_view()),
    path('register.html', views.SignUp.as_view()),
    path('logout.html', views.log_out),

    # 日志
    path('view_log/<str:log_date>/', views.view_log),
    path('view_log/', views.view_log),
    path('update_log/', views.update_log),
    path('access_log/', views.access_log),
    path('error_log/', views.error_log),

    # video
    path('upload/', views.upload),
    path('del_request/', views.del_request),
    path('add_vod/', views.add_vod),
    path('update_video/', views.update_video),
    path('update/', views.update),
    path('get_request/', views.get_request),
    path('get_carousel/', views.get_carousel),
    path('add_carousel/', views.carousel_add),
    path('del_carousel/', views.carousel_del),
    path('get_rating/', views.get_douban_rating),
    path('update_rating/', views.update_rating),
    path('get_80s_rating/', views.get_80s_rating),
    path('get_rating_by_name/', views.get_rating_by_name),
    path('set_rating/', views.set_rating),
    path('set_admin_flag/', views.admin_flag),
    path('get_douban_data/', views.get_douban_data),

    # 其他
    path('url2_clear/', views.url2_clear),
    path('url_clear/', views.url_clear),
    path('test/', views.test),
    path('', views.admin)
]
