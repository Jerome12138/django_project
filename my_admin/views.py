from django.shortcuts import render, HttpResponse, redirect
import json
from django.views import View
from django import forms
from django.forms import ModelForm
from django.forms import fields as Ffields
from django.forms import widgets as Fwidgets
from . import models
# Create your views here.


class UserInfoModelForm(ModelForm):
    confirm_pwd = Ffields.CharField(
        label='确认密码',
        widget=Fwidgets.PasswordInput(
            attrs={'placeholder': '请确认密码', 'class': "form-control form-control-sm"})
    )

    class Meta:
        model = models.UserInfo
        fields = ['email', 'username', 'nickname', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': "需要通过邮件激活账户", 'class': "form-control form-control-sm"}),
            'username': forms.TextInput(attrs={'placeholder': '登录用户名', 'class': "form-control form-control-sm"}),
            'nickname': forms.TextInput(attrs={'placeholder': '昵称', 'class': "form-control form-control-sm"}),
            'password': forms.PasswordInput(attrs={'placeholder': '至少7位，必须包含数字、字母', 'class': "form-control form-control-sm"}),
        }


# 注册
class SignUp(View):

    def get(self, request):
        user_modelform = UserInfoModelForm()
        return render(request, 'register.html', {'user_modelform': user_modelform})

    def post(self, request):
        user_modelform = UserInfoModelForm(request.POST)
        if user_modelform.is_valid():
            # user_modelform.save()
            print('添加用户：%s' % user_modelform.cleaned_data['username'])
            return redirect('/admin/login.html')
        else:
            print(user_modelform.errors.as_json())
            return render(request, 'register.html', {'user_modelform': user_modelform})


# 登录
class SignIn(View):
    def get(self, request):
        request.session.clear()
        return render(request, 'login.html', {'error_msg': ''})

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
                        if remember_me:
                            request.session.set_expiry(43200)
                    else:
                        ret['error'] = '用户名或密码错误'
        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '未知错误'
        finally:
            return HttpResponse(json.dumps(ret))


def log_out(request):   # 注销
    request.session.clear()
    return redirect('/admin/login.html')


def auth(func):   # 登录验证
    def inner(request, *args, **kwargs):
        username = request.session.get('username', None)
        if not username:
            return redirect('/admin/login.html')
        user_obj = models.UserInfo.objects.filter(username=username).first()
        return func(request, *args, **kwargs)  
    return inner


@auth
def admin(request):     # 管理页面
    return redirect('/video/admin/view_log/')


@auth
def upload(request):     # 上传页面
    ret = {'status': False, 'error': None, 'data': None}
    try:
        if request.method == "POST":
            file_obj = request.FILES.get('uploadFile')
            if file_obj:
                with open('file_storage/%s' % (file_obj.name), 'wb') as f:
                    if file_obj.multiple_chunks:
                        for i in file_obj.chunks():
                            f.write(i)
                    else:
                        f.write(file_obj.read())
                    print('文件"%s"上传成功(%sKB)'%(file_obj.name,round(file_obj.size/1024,2)))
                ret['status'] = True
            else:
                ret['status'] = False
                ret['error'] = '后台未收到文件'
    except Exception as e:
        print('Exception:',e)
        ret['status'] = False
        ret['error'] = '遇到异常'+e
    finally:
        return HttpResponse(json.dumps(ret))
