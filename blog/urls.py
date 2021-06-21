__author__ = "Jerome"

from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from . import backend_views

backend_patterns = [
    path('info/', backend_views.Info.as_view()),
    path('articles/', backend_views.Articles.as_view()),
    path('tag/', backend_views.Tag.as_view()),
    path('category/', backend_views.Category.as_view()),
    path('edit_article/<int:article_id>/', backend_views.EditArticle.as_view()),
    path('add_article/', backend_views.EditArticle.as_view()),
    path('add_comment/<int:article_id>/', backend_views.AddComment.as_view()),
    path('del_comment/', backend_views.Comment.as_view()),
    path('', backend_views.Info.as_view()),
]

user_patterns = [
    path('articles/<int:var>.html', views.article),
    re_path(
        'articles/(?P<condition>((date)|(tag)|(category)))/(?P<var>[\w-]+).html', views.filter),
    path('', views.home),
]

urlpatterns = [
    path('sign_in/', views.SignIn.as_view()),
    path('sign_up/', views.SignUp.as_view()),
    path('log_out/', views.log_out),
    path('work_test/', views.work_test),
    # path('check_code/', views.check_code),
    path('backend/', include(backend_patterns)),
    path('<str:username>/', include(user_patterns)),
    path('', views.index)
]
