from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
from django.views import View
from django import forms
from django.forms import ModelForm
from django.forms import fields as Ffields
from django.forms import widgets as Fwidgets
from . import models
import json


class UserInfoModelForm(ModelForm):
    confirm_pwd = Ffields.CharField(
        label='确认密码',
        widget=Fwidgets.PasswordInput(attrs={'placeholder': '请确认密码','class':"form-control form-control-sm"})
    )

    class Meta:
        model = models.UserInfo
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "需要通过邮件激活账户",'class':"form-control form-control-sm"}),
            'username': forms.TextInput(attrs={'placeholder': '登录用户名','class':"form-control form-control-sm"}),
            'nickname': forms.TextInput(attrs={'placeholder': '昵称','class':"form-control form-control-sm"}),
            'password': forms.PasswordInput(attrs={'placeholder': '至少7位，必须包含数字、字母','class':"form-control form-control-sm"}),
        }


# 注册
class SignUp(View):

    def get(self, request):
        user_modelform = UserInfoModelForm()
        return render(request, 'sign_up.html', {'user_modelform': user_modelform})

    def post(self, request):
        user_modelform = UserInfoModelForm(request.POST)
        if user_modelform.is_valid():
            user_modelform.save()
            print('添加用户：%s' % user_modelform.cleaned_data['username'])
            return redirect('/blog/' + user_modelform.cleaned_data['username'])
        else:
            print(user_modelform.errors.as_json())
            return render(request, 'sign_up.html', {'user_modelform': user_modelform})


# 登录
class SignIn(View):
    def get(self, request):
        request.session.clear()
        return render(request, 'sign_in.html', {'error_msg': ''})

    def post(self, request):
        ret = {'status': False, 'error': None, 'data': None}
        try:
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)
            remember_me = request.POST.get('remember-me', None)
            if not username or not password:
                ret['error'] = '请输入用户名和密码'
            else:
                user_obj = models.UserInfo.objects.filter(
                    username=username).first()
                if not user_obj:
                    ret['error'] = '用户名或密码错误'
                else:
                    if user_obj.password == password:
                        ret['status'] = True
                        ret['data'] = {'username': username}
                        request.session['username'] = username
                        request.session['is_login'] = True
                        if not remember_me:
                            request.session.set_expiry(0)
                    else:
                        ret['error'] = '用户名或密码错误'
        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '未知错误'
        finally:
            return HttpResponse(json.dumps(ret))


# 注销
def log_out(request):
    request.session.clear()
    return redirect('/blog/sign_in/')


# 首页
def index(request):
    return render(request, 'index.html')


# 获取日期列表
def get_date_list():
    date_list = models.Article.objects.raw(
        'select id, count(id) as num, strftime("%Y-%m",create_time) as ctime from blog_article group by strftime("%Y-%m",create_time)')
    return date_list


# 博主主页
def home(request, username):
    user_obj = models.UserInfo.objects.filter(username=username).first()
    if not user_obj:
        redirect('/blog/')
    article_objs = models.Article.objects.filter(user=user_obj).all()
    return render(request, 'home_list.html',
                  {
                      'user_obj': user_obj,
                      'article_objs': article_objs,
                      'date_list': get_date_list()
                  })


# 文章详情页
def article(request, username, var):
    article_obj = models.Article.objects.filter(id=var).first()
    user_obj = models.UserInfo.objects.filter(username=username).first()
    if article_obj.user == user_obj:  # 用户名相符
        from .backend_views import CommentForm
        comment_form = CommentForm()
        return render(request, 'home_article_detail.html', {
            'user_obj': user_obj,
            'article_obj': article_obj,
            'date_list': get_date_list(),
            'comment_form': comment_form,
        })
    else:
        return HttpResponse('文章不存在')


# 筛选
def filter(request, username, condition, var):
    user_obj = models.UserInfo.objects.filter(username=username).first()
    if not user_obj:
        return redirect('/blog/')
    if condition == 'category':
        article_objs = models.Article.objects.filter(
            user=user_obj, category__name=var).all()
    elif condition == 'date':
        year, month = var.split('-')
        article_objs = models.Article.objects.filter(user=user_obj, create_time__year=year,
                                                     create_time__month=month).all()
    elif condition == 'tag':
        tag_obj = models.Tag.objects.filter(name=var).first()
        article_objs = models.Article.objects.filter(
            user=user_obj, tags=tag_obj).all()
    else:
        return redirect('/blog/')
    return render(request, 'home_list.html', {
        'user_obj': user_obj,
        'article_objs': article_objs,
        'date_list': get_date_list()
    })

    
def work_test(request):
    return render(request, 'work_test/index.html')