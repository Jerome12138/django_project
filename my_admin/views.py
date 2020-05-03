import json
import time
import os
import random

from django.shortcuts import render, HttpResponse, redirect
from django.http.response import JsonResponse
from django.views import View
from django import forms
from django.forms import ModelForm
from django.forms import fields as Ffields
from django.forms import widgets as Fwidgets

from video.func.pagination import Page
from video.func import GetPageData
from video.func import DBHandler
from . import models
from .func import webpToJPG
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
            # print(ret)
            return HttpResponse(json.dumps(ret))


def log_out(request):   # 注销
    request.session.clear()
    return redirect('/admin/login.html')


def auth(func):   # 登录验证
    def inner(request, *args, **kwargs):
        username = request.session.get('username', None)
        if not username:
            return redirect('/admin/login.html')
        # user_obj = models.UserInfo.objects.filter(username=username).first()
        return func(request, *args, **kwargs)
    return inner


@auth
def admin(request):     # 管理页面
    return render(request, 'admin_home.html')


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
                    print('文件"%s"上传成功(%sKB)' %
                          (file_obj.name, round(file_obj.size/1024, 2)))
                ret['status'] = True
            else:
                ret['status'] = False
                ret['error'] = '后台未收到文件'
    except Exception as e:
        print('Exception:', e)
        ret['status'] = False
        ret['error'] = '遇到异常'+e
    finally:
        return HttpResponse(json.dumps(ret))


@auth
def get_request(request):  # 用户请求
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = DBHandler.load_request_data()
    data_count = len(data_list)
    page = Page(request.path_info+'?page=', page_index, data_count//24 + 1)
    page_str = page.page_str()
    request_list = page.video_page(data_list, 24)
    if request_list == -1:
        return HttpResponse('请求错误')
    return render(request, 'admin_requests.html', {
        "request_list": request_list,
        'page_str': page_str,
        "data_count": data_count
    })


@auth
def del_request(request):   # 删除请求
    ret = {'status': True, 'error': None, 'data': None}
    try:
        vod_id = request.POST.get('vod_id')
        DBHandler.del_request_data(vod_id)
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = e
    finally:
        return HttpResponse(json.dumps(ret))


@auth
def add_vod(request):   # 添加视频数据
    ret = {'status': True, 'error': None, 'data': None}
    try:
        vod_id = request.POST.get('vod_id')
        vod_data = GetPageData.get_vod_data(vod_id)
        flag = DBHandler.dump_vod_data(vod_data)
        DBHandler.update_request_data(vod_id)
        if flag:
            ret['data'] = "已成功添加 %s !" % vod_data['vod_name']
        else:
            ret['status'] = False
            ret['error'] = "数据库操作出现错误"
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = e
    finally:
        return HttpResponse(json.dumps(ret))


@auth
def update_log(request):
    log_path = 'logs/update.log'
    log_str = DBHandler.load_log(log_path)
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = log_str.split('\n')
    data_count = len(data_list)
    page = Page(request.path_info+'?page=', page_index, data_count//100 + 1)
    page_str = page.page_str()
    log_list = page.video_page(data_list, 100)
    if log_list == -1:
        return HttpResponse('请求错误')
    log_str = '\n'.join(log_list)
    return render(request, 'admin_update_log.html', {
        "log": log_str,
        'page_str': page_str,
    })


@auth
def access_log(request):
    log_path = 'logs/nginx/web_access.log'
    log_str = DBHandler.load_log(log_path)
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = log_str.split('\n')
    data_count = len(data_list)
    page = Page(request.path_info+'?page=', page_index, data_count//100 + 1)
    page_str = page.page_str()
    log_list = page.video_page(data_list, 100)
    if log_list == -1:
        return HttpResponse('请求错误')
    log_str = '\n'.join(log_list)
    return render(request, 'admin_update_log.html', {
        "log": log_str,
        'page_str': page_str,
    })


@auth
def error_log(request):
    log_path = 'logs/nginx/web_error.log'
    log_str = DBHandler.load_log(log_path)
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = log_str.split('\n')
    data_count = len(data_list)
    page = Page(request.path_info+'?page=', page_index, data_count//100 + 1)
    page_str = page.page_str()
    log_list = page.video_page(data_list, 100)
    if log_list == -1:
        return HttpResponse('请求错误')
    log_str = '\n'.join(log_list)
    return render(request, 'admin_update_log.html', {
        "log": log_str,
        'page_str': page_str,
    })


@auth
def view_log(request, log_date=0):
    # 加载log文件
    if log_date == 0:
        log_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        is_today = True
        log_path = 'uwsgi.log'
    elif log_date == time.strftime("%Y-%m-%d", time.localtime(time.time())):
        is_today = True
        log_path = 'uwsgi.log'
    else:
        is_today = False
        month = "-".join(log_date.split('-')[0:2])
        log_path = 'logs/%s/uwsgi-%s.log' % (month, log_date)
        if not(os.path.exists(log_path) and os.path.isfile(log_path)):
            log_str = '当天无日志'
            return render(request, 'admin_log.html', {
                "log": log_str,
                'log_date': log_date,
                'is_today': is_today,
                'page_str': '',
            })
    log = DBHandler.load_log(log_path)
    # 剔除部分字段
    import re
    log = re.sub(
        r'(\*\*\*\sStarting\suWSGI.+?interpreter\smode\s\*\*\*)', '*** Starting uWSGI ***', log, flags=re.DOTALL)
    log = re.sub(r'(nsukey\=.+)', '<<wechat>>', log)
    log = re.sub(r'(\[pid:.+?\.php.+?\(HTTP\/1\.1\s404\).+\n)', '', log)
    log = re.sub(
        r'(\[pid:.+?GET\s\/\s\=\>\sgenerated.+?\(HTTP\/1\.1\s404\).+\n)', '', log)
    log = re.sub(r'(\[pid.+?\])', '', log)
    log = re.sub(r'(\(\)\s\{.+?bytes\})', '', log)
    log = re.sub(r'(\d+?\sheaders\sin.+?\))', '', log)
    log = re.sub(r'(generated.+?msecs)', '', log)
    log = re.sub(r'(\=\>\s+?\(HTTP\/1\.1\s200\))', '', log)
    log = re.sub(r'(\s\[\w{3}\s\w{3}\s\d{1,2}\s)', '[', log)
    log = re.sub(r'(\s\d{4}\]\s)', ']', log)
    log_str = re.sub(r'(.+?\(HTTP\/1\.1\s30\d\).+\n)', '', log)
    # print(log_str)
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = log_str.split('\n')
    data_count = len(data_list)
    page = Page(request.path_info+'?page=', page_index, data_count//100 + 1)
    page_str = page.page_str()
    log_list = page.video_page(data_list, 100)
    if log_list == -1:
        return HttpResponse('请求错误')
    log_str = '\n'.join(log_list)
    if log_date == 0:
        log_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
    return render(request, 'admin_log.html', {
        "log": log_str,
        'log_date': log_date,
        'is_today': is_today,
        'page_str': page_str,
    })


@auth
def update_video(request):
    pass
    return render(request, 'admin_update.html')


@auth
def update(request):    # 更新视频数据 最大资源网
    ret = {'status': True, 'error': None, 'data': None}
    try:
        url_index = request.GET.get('url_index', None)
        up_type = request.GET.get('type', None)
        # 设定url前缀
        if url_index == '1':
            url_temp = "http://www.zdziyuan.com/inc/s_feifei3zuidam3u8/?p=%s"
        elif url_index == '2':
            url_temp = "http://cj.bajiecaiji.com/inc/feifei3bjm3u8/index.php?p=%s"
        else:
            raise Exception('url参数错误')
        get_all_data = GetPageData.getAllData(url_temp, int(url_index))
        if up_type == 'today':    # 更新当日
            update_count = get_all_data.run()
        elif up_type == 'all':   # 更新全部
            update_count = get_all_data.run(flag=1)
        elif up_type == 'count':
            up_count = request.GET.get('count', None)
            if up_count is None or not up_count.isdigit():
                up_count = 1000
            else:
                up_count = int(up_count)
            update_count = get_all_data.run(up_count=up_count)
        else:
            raise Exception('type参数错误')
        ret['data'] = '已更新%s条数据' % update_count
    except Exception as e:
        print('Exception:', e)
        ret['status'] = False
        ret['error'] = 'Exception: %s' % e
    finally:
        return HttpResponse(json.dumps(ret))


@auth
def url2_clear(request):
    DBHandler.clear_url2()
    return HttpResponse('已清空值为1的url2')


@auth
def url_clear(request):
    DBHandler.clear_url()
    return HttpResponse('已清空值为1的url')


def _auto_update():
    get_all_data = GetPageData.getAllData(
        "http://www.zdziyuan.com/inc/s_feifei3zuidam3u8/?p=%s")
    get_all_data.run()
    get_all_data2 = GetPageData.getAllData(
        "http://cj.bajiecaiji.com/inc/feifei3bjm3u8/index.php?p=%s", 2)
    get_all_data2.run()


@auth
def get_carousel(request):  # 用户请求
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = DBHandler.load_carousel_data()
    data_count = len(data_list)
    page = Page(request.path_info+'?page=', page_index, data_count//24 + 1)
    page_str = page.page_str()
    carousel_list = page.video_page(data_list, 24)
    if carousel_list == -1:
        return HttpResponse('请求错误')
    return render(request, 'admin_carousel.html', {
        "carousel_list": carousel_list,
        'page_str': page_str,
        "data_count": data_count
    })


@auth
def carousel_add(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        carousel_data = {}
        vod_id = request.POST.get('vod_id')
        if vod_id and vod_id.isdigit():
            carousel_data['vod_id'] = vod_id
        carousel_data['vod_name'] = request.POST.get('vod_name')
        carousel_data['vod_pic'] = request.POST.get('vod_pic')
        carousel_data['vod_url'] = request.POST.get('vod_url')
        carousel_data['vod_index'] = request.POST.get('vod_index')
        # print(carousel_data)
        # 转换为本地链接
        vod_pic = request.POST.get('vod_pic')
        if vod_pic and vod_pic.endswith('.webp'):
            jpg_path = webpToJPG.webp_to_jpg(vod_pic)
            carousel_data['vod_pic'] = jpg_path
        else:
            carousel_data['vod_pic'] = vod_pic
        flag = DBHandler.dump_carousel_data(carousel_data)
        if flag:
            ret['data'] = "已成功添加轮播图： %s !" % carousel_data['vod_name']
        else:
            ret['status'] = False
            ret['error'] = "数据库操作出现错误"
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = "未知错误"
    finally:
        return HttpResponse(json.dumps(ret))


def carousel_del(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        vod_id = request.POST.get('vod_id')
        DBHandler.del_carousel_data(vod_id)
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = e
    finally:
        return HttpResponse(json.dumps(ret))


@auth
def test(request):
    DBHandler.db_test()
    return HttpResponse('rep')


@auth
def get_douban_rating(request):
    data_list = []
    none_list = DBHandler.redis_loadlist('douban_none_list')
    res_status = False
    try:
        data_list.extend(DBHandler.load_type_data(**{'vod_cid': '1'}))    # 获取所有电影
        # data_list.extend(DBHandler.load_type_data(**{'vod_cid': '2'}))  # 获取所有电视剧
        timeout=0
        for item in data_list:
            if item['vod_douban_id'] is None and item['vod_id'] not in none_list:  # 不存在豆瓣id，则查找id
            #     print(item['vod_douban_id'],item['vod_rating'])
            # if False:
                # douban_id = GetPageData.findID('爱情公寓2','2011')    # test network
                douban_id = GetPageData.findID(item['vod_name'], item['vod_year'])
                if douban_id:   # 如果查找到豆瓣id
                    timeout = 0
                    # print(douban_id)
                    DBHandler.dump_douban_id(item['vod_id'], douban_id)
                    rating = GetPageData.getRating(douban_id)
                    print(item['vod_name'], douban_id, rating)
                    DBHandler.dump_rating(item['vod_id'], rating)
                    # 防止账号被封，随机延迟
                    time.sleep(3 + float(random.randint(40, 100)) / 20)
                else:   # 未查找到豆瓣id
                    test_net = GetPageData.findID('爱情公寓2', '2011')
                    if test_net is None:
                        print('----------地址被限制,稍后重试----------')
                        if none_list:
                            DBHandler.redis_dumplist('douban_none_list',none_list)
                        time.sleep(60)
                        timeout+=1
                        if timeout == 5:
                            print('连续五次失败，等待5分钟')
                            time.sleep(300)
                        elif timeout>10:
                            print('-----连续十次失败，退出-----')
                            break
                        print('----------重新启动查找------------')
                    else:
                        print(item['vod_name'],'无豆瓣id数据，存入列表')
                        none_list.append(item['vod_id'])
        res_status = True
    except Exception as e:
        print('redis_dump exception:',e)
        res_status = 'redis_dump exception:%s'%e
    finally:
        if none_list:
            DBHandler.redis_dumplist('douban_none_list',none_list)
        return HttpResponse(res_status)
