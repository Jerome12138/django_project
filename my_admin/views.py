import json
import time
import os
import random
import traceback
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
    invite_code = Ffields.CharField(
        label='邀请码',
        widget=Fwidgets.PasswordInput(
            attrs={'placeholder': '联系管理员1030155707@qq.com获取邀请码', 'class': "form-control form-control-sm"})
    )
    def clean_confirm_pwd(self):
        if self.cleaned_data['confirm_pwd'] != self.cleaned_data['password']:
            raise forms.ValidationError('确认密码输入错误')
        return self.cleaned_data['confirm_pwd']
    
    def clean_invite_code(self):
        if self.cleaned_data['invite_code'] not in ['jerome001','jerome002','jerome003','jerome004']:
            raise forms.ValidationError('邀请码无效')
        return self.cleaned_data['invite_code']

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
        ret = {'status': False, 'error': None, 'data': None}
        try:
            
            user_modelform = UserInfoModelForm(request.POST)
            if user_modelform.is_valid():
                ret['status'] = True
                ret['data'] = {'username': user_modelform.cleaned_data['username']}
                user_modelform.save()
                print('添加用户：%s' % user_modelform.cleaned_data['username'])
            else:
                ret['status'] = False
                ret['error'] = user_modelform.errors.as_text()
                print(user_modelform.errors.as_json())
                return render(request, 'register.html', {'user_modelform': user_modelform})
        except Exception as e:
            print(e)
            ret['status'] = False
            ret['error'] = '未知错误'
        finally:
            # print(ret)
            return HttpResponse(json.dumps(ret))




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
            # print(username+'登录')
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
        return redirect('/view_log/%s/' % log_date)
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
                up_count = 3000
            else:
                up_count = int(up_count)
            update_count = get_all_data.run(up_count=up_count)
        else:
            raise Exception('type参数错误')
        ret['data'] = '已更新%s条数据' % update_count
    except Exception as e:
        print('my_admin update Exception:', e)
        print(traceback.print_exc())
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
    rep = DBHandler.db_test()
    return HttpResponse(rep)


@auth
def admin_flag(request):
    admin_flag = request.GET.get('flag')
    rep = DBHandler.redis_dump('admin_flag', admin_flag)
    print('管理员设置：%s' % admin_flag)
    return HttpResponse(rep)


@auth
def update_rating(request):
    res_status = False
    try:
        print('————————开始更新豆瓣评分数据————————')
        data_list = DBHandler.get_none_rating()    # 获取所有电影
        for item in data_list:
            # 判断管理员指令
            admin_flag = DBHandler.redis_load('admin_flag')
            if admin_flag == b'0':
                print('管理员终止')
                break
            douban_id = item['vod_douban_id']
            rating = GetPageData.getRating(douban_id)
            if rating:
                DBHandler.dump_rating(item['vod_id'], rating)
                print(item['vod_name'], 
                      rating, '保存成功[rating]')
        res_status = True
    except Exception as e:
        print('update_rating exception:', e)
        print(traceback.print_exc())
        res_status = 'update_rating exception:%s' % e
    finally:
        print('————————豆瓣评分数据更新完毕————————')
        return HttpResponse(res_status)


@auth
def get_douban_rating(request):
    res_status = False
    flag = True
    timeout = 0
    try:
        print('————————开始获取豆瓣id数据————————')
        # data_list = DBHandler.load_type_data(
        #     **{'vod_cid': '1', 'no_douban_id': True})    # 获取所有电影
        data_list = DBHandler.load_type_data(**{'vod_cid': '2', 'no_douban_id': True})  # 获取所有电视剧
        none_list = DBHandler.redis_loadlist('douban_none_list')
        none_list2 = DBHandler.redis_loadlist('douban_none_list2')
        print('无豆瓣id的视频总数：%s' % len(data_list))
        print('无匹配视频总数：%s' % len(none_list))
        print('重复数据的视频总数：%s' % len(none_list2))
        # while flag:
        # print(bytes('75519',encoding='utf-8') not in none_list and bytes('75519',encoding='utf-8') not in none_list2)
        # return HttpResponse(none_list)
        for item in data_list:
            admin_flag = DBHandler.redis_load('admin_flag')
            if admin_flag == b'0':
                print('管理员终止')
                break
            b_id = bytes(item['vod_id'], encoding='utf-8')
            # 不存在豆瓣id，则查找id
            if item['vod_douban_id'] is None and (b_id not in none_list and b_id not in none_list2):
                # print(item['vod_douban_id'],item['vod_rating'])
                i = 0
                while i < 2:
                    douban_id = GetPageData.findID(
                        item['vod_name'], item['vod_year'])
                    if douban_id:   # 如果查找到豆瓣id
                        timeout = 0
                        if type(douban_id) == list:
                            print(item['vod_name'],
                                  '匹配到多个豆瓣id数据，存入列表2', douban_id)
                            if b_id not in none_list2:
                                none_list2.append(b_id)
                        else:
                            DBHandler.dump_douban_id(item['vod_id'], douban_id)
                            print(item['vod_name'], douban_id, end=' ')
                            rating = GetPageData.getRating(douban_id)
                            if rating:
                                print(rating, end='')
                                DBHandler.dump_rating(item['vod_id'], rating)
                            print('保存成功[douban]')
                        # 防止账号被封，随机延迟
                        # time.sleep(1 + float(random.randint(40, 100)) / 20)
                        time.sleep(0.5)
                        break
                    else:   # 未查找到豆瓣id
                        i += 1
                        # if i ==1:
                        #     print(item['vod_name'])
                        continue
                        # test_net = GetPageData.findID('爱情公寓2', '2011')
                        # if test_net is None:    # 网络异常
                        # print('----------地址被限制,稍后重试----------')
                        #     if none_list:
                        #         DBHandler.redis_dumplist(
                        #             'douban_none_list', none_list)
                        #         none_list = []
                        #         print('none_list 暂存')
                        #     if none_list2:
                        #         DBHandler.redis_dumplist(
                        #             'douban_none_list2', none_list2)
                        #         none_list2 = []
                        #         print('none_list2 暂存')
                        #     # time.sleep(180)
                        #     timeout += 1
                        #     # if timeout == 5:
                        #     #     print('连续五次失败，等待30分钟')
                        #     #     time.sleep(1800)
                        #     #     print('----------重新启动查找------------')
                        #     #     continue
                        #     # elif timeout >= 10:
                        #     #     print('-----连续十次失败，等待1小时-----')
                        #     #     time.sleep(3600)
                        #     #     timeout = 0
                        #     #     continue
                        # else:
                        #     print(item['vod_name'], '无豆瓣id数据，存入列表')
                        #     if b_id not in none_list:
                        #         none_list.append(b_id)
        res_status = True
    except Exception as e:
        print('get_douban_rating exception:', e)
        print(traceback.print_exc())
        res_status = 'get_douban_rating exception:%s' % e
    finally:
        if none_list:
            DBHandler.redis_dumplist('douban_none_list', none_list)
        if none_list2:
            DBHandler.redis_dumplist('douban_none_list2', none_list2)
        DBHandler.redis_dump('admin_flag', '1')
        print('————————豆瓣id获取完毕————————')
        return HttpResponse(res_status)


@auth
def get_80s_rating(request):
    get_80s_score = GetPageData.Get80sScore()
    get_80s_score.run()
    return HttpResponse('res')


@auth
def get_rating_by_name(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        vod_id = request.POST.get('vod_id')
        vod_name = request.POST.get('vod_name')
        vod_year = request.POST.get('vod_year')
        douban_id = GetPageData.findID(vod_name, vod_year)
        if douban_id:   # 如果查找到豆瓣id
            ret['data'] = douban_id
            if type(douban_id) == list:
                ret['status'] = False
                ret['error'] = '存在多个数据'
            else:
                DBHandler.dump_douban_id(vod_id, douban_id)
                print(vod_name, douban_id, end=' ')
                rating = GetPageData.getRating(douban_id)
                if rating:
                    print(rating, end='')
                    DBHandler.dump_rating(vod_id, rating)
                print('保存成功[douban]')
        else:   # 未查找到豆瓣id
            ret['status'] = False
            test_net = GetPageData.findID('爱情公寓2', '2011')
            if test_net is None:    # 网络异常
                ret['error'] = '地址被限制,请稍后重试'
            else:
                ret['error'] = '无豆瓣id数据'
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = e
    finally:
        return HttpResponse(json.dumps(ret))


@auth
def set_rating(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        vod_id = request.GET.get('vod_id')
        douban_id = request.GET.get('douban_id')
        if douban_id:   # 如果查找到豆瓣id
            ret['data'] = douban_id
            if type(douban_id) == list:
                ret['status'] = False
                ret['error'] = '存在多个数据'
            else:
                rating = GetPageData.getRating(douban_id)
                print(vod_id, douban_id, rating, end='')
                DBHandler.dump_douban_id(vod_id, douban_id)
                DBHandler.dump_rating(vod_id, rating)
                print('保存成功[douban]')
        else:   # 未查找到豆瓣id
            ret['status'] = False
            test_net = GetPageData.findID('爱情公寓2', '2011')
            if test_net is None:    # 网络异常
                ret['error'] = '地址被限制,请稍后重试'
            else:
                ret['error'] = '无豆瓣id数据'
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = e
    finally:
        return HttpResponse(json.dumps(ret))

@auth
def get_douban_data(request):
    GetPageData.get_douban_data()
    return HttpResponse('res')

@auth
# 匹配豆瓣json数据
def match_douban_data(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        type_list = ['movie','tv']
        tag_list = {
            'movie': ['热门','最新','经典','华语','欧美','韩国','日本','动作','喜剧','爱情','科幻','悬疑','恐怖','治愈'],
            'tv': ['热门','美剧','英剧','日剧','国产剧','港剧','日本动画','综艺','纪录片']
        }
        for video_type in type_list:
            admin_flag = DBHandler.redis_load('admin_flag')
            if admin_flag == b'0':
                print('管理员终止')
                break
            for tag in tag_list[video_type]:
                admin_flag = DBHandler.redis_load('admin_flag')
                if admin_flag == b'0':
                    print('管理员终止')
                    break
                filename = 'douban/%s_%s.json' % (video_type, tag)
                with open(filename,'r',encoding='utf-8') as f:
                    detail_list = json.load(f)
                for item in detail_list['subjects']:
                    GetPageData.match_score_by_name(item)
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = e
    finally:
        return HttpResponse(json.dumps(ret))

# 匹配豆瓣json数据，从网络搜集到的豆瓣数据集
@auth
def match_douban_json_data(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        with open('douban/douban_data.json','r',encoding='utf-8') as f:
            douban_list = json.load(f)
        for item in douban_list:
            GetPageData.match_score_from_jsondata(item)
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = e
    finally:
        return HttpResponse(json.dumps(ret))

# 删除错误的豆瓣数据
@auth
def remove_douban_data(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        vod_id = request.GET.get('vod_id', None)
        if not vod_id:
            ret['status'] = False
            return
        DBHandler.dump_douban_id(vod_id, None)
        DBHandler.dump_rating(vod_id, None)
        ret['data'] = "已成功删除豆瓣数据"
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = e
    finally:
        return HttpResponse(json.dumps(ret))
