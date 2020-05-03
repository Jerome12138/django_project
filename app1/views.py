from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from app1 import models
import json


# Create your views here.

user_list = {}

def sign_in(request):
    if request.method == 'GET':
        res = render(request, 'sign_in.html')
    elif request.method == 'POST':
        email = request.POST.get('email', None)
        pwd = request.POST.get('pwd', None)
        if email == 'root@163.com' and pwd == '123':
            res = redirect('/app1/record/')
            res.set_cookie('user', 'dasdasdasdasdaw')
            print('已设置cookie')
        else:
            error_msg = '用户名或密码错误'
            res = render(request, 'sign-in.html', {'error_msg': error_msg})
    else:
        error_msg = '其他方式暂不支持'
        res = render(request, 'sign-in.html', {'error_msg': error_msg})
    return res


def auth(func):
    def inner(request, *args, **kwargs):
        # request.COOKIES.clear()
        cookie = request.COOKIES.get('user')
        if cookie == 'null' or not cookie:
            print('没有cookie')
            return redirect('/app1/sign-in/')
        print(cookie)
        return func(request, *args, **kwargs)
    return inner


@auth
def record(request):
    cookie = request.COOKIES.get('user')
    if cookie =='dasdasdasdasdaw':
        user_name = '张俊龙'
    else:
        user_name = '未知用户'
    data = models.WorkData.objects.all()
    return render(request, 'job_record.html', {'data': data,'user_name':user_name})


from .pagination import Page

@auth
def detail(request, **kwargs):
    ret = {'status': True, 'error': None, 'data': None}
    if request.method == 'GET':
        # 获取用户cookie
        cookie = request.COOKIES.get('user')
        if cookie == 'dasdasdasdasdaw':
            user_name = '张俊龙'
        else:
            user_name = '未知用户'
        # 获取页面数据
        id = int(request.GET.get('p', 1))
        data_dict = models.WorkData.objects.filter(id=id).first().__dict__
        field_dict = {}
        for field in models.WorkData._meta.fields:
            if field.name == 'status':
                status = models.WorkData.objects.filter(id=id).first().status.status
                field_dict['status'] = ['状态', status]
            else:
                field_dict[field.name] = [field.verbose_name, data_dict[field.name]]
        count = models.WorkData.objects.all().count()
        # Status类
        status_list = models.Status.objects.all()

        page = Page(id, count, 1)
        page_str = page.page_str('/app1/detail/')
        return render(request, 'job_detail.html',
                      {'field_dict': field_dict, 'page_str': page_str, 'status_list': status_list,'user_name':user_name})
    elif request.method == 'POST':
        data_dict = {}
        try:
            id = request.POST.get('id')
            if id == 'new':  # 添加新数据
                for field in models.WorkData._meta.fields:
                    if field.name == 'id':
                        continue
                    elif field.name == 'status':
                        data_dict['status_id'] = request.POST.get('status_id')
                    else:
                        data_dict[field.name] = request.POST.get(field.name)
                models.WorkData.objects.create(**data_dict)
            else:  # 编辑数据
                data = models.WorkData.objects.filter(id=id).first()
                if not data:
                    ret['status'] = False
                    ret['error'] = '该用户组不存在或已被删除'
                else:
                    for field in models.WorkData._meta.fields:
                        if field.name == 'status':
                            data_dict['status_id'] = request.POST.get('status_id')
                        else:
                            data_dict[field.name] = request.POST.get(field.name)
                    print(data_dict)
                    models.WorkData.objects.filter(id=id).update(**data_dict)
        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '未知错误'
        finally:
            return HttpResponse(json.dumps(ret))
