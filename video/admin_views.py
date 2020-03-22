from django.shortcuts import render, redirect, HttpResponse
from django.http.response import JsonResponse

from video import models
from .func.GetPageData import *
from .func.db_handler import *
from .func.pagination import Page
import time
import json
import os

# Create your views here.
# 登录验证
def auth(func):
    def inner(request, *args, **kwargs):
        username = request.session.get('username', None)
        if not username:
            return redirect('/admin/login.html')
        # user_obj = models.UserInfo.objects.filter(username=username).first()
        return func(request, *args, **kwargs) #user_obj,
    return inner

@auth
def get_request(request):# 用户请求
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = load_request_data()
    data_count = len(data_list)
    page = Page('/video/admin/?page=', page_index, data_count//24 + 1)
    page_str = page.page_str()
    request_list =page.video_page(data_list,24)
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
        del_request_data(vod_id)
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
        # print(vod_id)
        vod_data = get_vod_data(vod_id)
        # print(vod_id,vod_data)
        flag = dump_vod_data(vod_data)
        update_request_data(vod_id)
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
    log = load_log(log_path)
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
    page = Page('/video/admin/view_log/%s/?page='%log_date, page_index, data_count//100 + 1)
    page_str = page.page_str()
    log_list =page.video_page(data_list,100)
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
    return render(request,'admin_update.html')

@auth
def update(request):    # 更新视频数据 最大资源网
    ret = {'status': True, 'error': None, 'data': None}
    try:
        get_all_data = getAllData("http://www.zdziyuan.com/inc/s_feifei3zuidam3u8/?p=%s")
        if request.GET.get('flag'):
            updata_count = get_all_data.run(flag=1)
        else:
            updata_count = get_all_data.run()
        ret['data'] = '已更新%s条数据' % updata_count
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = "未知错误"
    finally:
        return HttpResponse(json.dumps(ret))

@auth
def update2(request):   # 更新第二url(八戒资源网)
    ret = {'status': True, 'error': None, 'data': None}
    try:
        get_all_data = getAllData("http://cj.bajiecaiji.com/inc/feifei3bjm3u8/index.php?p=%s",2)
        if request.GET.get('flag'): # 更新全部
            updata_count = get_all_data.run2(flag=1)
        else:   # 更新当日
            updata_count = get_all_data.run2(flag=1)
        ret['data'] = '已更新%s条数据' % updata_count
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = "未知错误"
    finally:
        return HttpResponse(json.dumps(ret))

@auth
def url2_clear(request):
    clear_url2()
    return HttpResponse('已清空值为1的url2')

@auth
def url_clear(request):
    clear_url()
    return HttpResponse('已清空值为1的url')

@auth
def test(request):
    db_test()
    return HttpResponse('test完成')