from django.shortcuts import render, redirect, HttpResponse
from django.http.response import JsonResponse

from video import models
from .func.GetPageData import get_vod_data,getAllData
from .func.db_handler import update_request_data,load_request_data,del_request_data
from .func.db_handler import dump_vod_data,load_log,clear_url2,clear_url,db_test
from .func.db_handler import dump_carousel_data,load_carousel_data,del_carousel_data
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
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = load_request_data()
    data_count = len(data_list)
    page = Page(request.path_info+'?page=', page_index, data_count//24 + 1)
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
def update_log(request):
    log_path = 'logs/update.log'
    log_str = load_log(log_path)
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = log_str.split('\n')
    data_count = len(data_list)
    page = Page(request.path_info+'?page=', page_index, data_count//100 + 1)
    page_str = page.page_str()
    log_list =page.video_page(data_list,100)
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
    log_str = load_log(log_path)
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = log_str.split('\n')
    data_count = len(data_list)
    page = Page(request.path_info+'?page=', page_index, data_count//100 + 1)
    page_str = page.page_str()
    log_list =page.video_page(data_list,100)
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
    log_str = load_log(log_path)
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = log_str.split('\n')
    data_count = len(data_list)
    page = Page(request.path_info+'?page=', page_index, data_count//100 + 1)
    page_str = page.page_str()
    log_list =page.video_page(data_list,100)
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
    page = Page(request.path_info+'?page=', page_index, data_count//100 + 1)
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
        url_index = request.GET.get('url_index',None)
        up_type = request.GET.get('type',None)
        # 设定url前缀
        if url_index == '1':
            url_temp = "http://www.zdziyuan.com/inc/s_feifei3zuidam3u8/?p=%s"
        elif url_index == '2':
            url_temp = "http://cj.bajiecaiji.com/inc/feifei3bjm3u8/index.php?p=%s"
        else:
            raise Exception('url参数错误')
        get_all_data = getAllData(url_temp,int(url_index))
        if up_type=='today':    # 更新当日
            update_count = get_all_data.run()
        elif up_type =='all':   # 更新全部
            update_count = get_all_data.run(flag=1)
        elif up_type =='count':
            up_count = request.GET.get('count',None)
            if up_count is None or not up_count.isdigit():
                up_count = 1000
            else:
                up_count = int(up_count)
            update_count = get_all_data.run(up_count=up_count)
        else:
            raise Exception('type参数错误')
        ret['data'] = '已更新%s条数据' % update_count
    except Exception as e:
        print('Exception:',e)
        ret['status'] = False
        ret['error'] = 'Exception: %s'%e
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

@auth
def _auto_update():
    get_all_data = getAllData("http://www.zdziyuan.com/inc/s_feifei3zuidam3u8/?p=%s")
    get_all_data.run()
    get_all_data2 = getAllData("http://cj.bajiecaiji.com/inc/feifei3bjm3u8/index.php?p=%s",2)
    get_all_data2.run()

@auth
def get_carousel(request):# 用户请求
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = load_carousel_data()
    data_count = len(data_list)
    page = Page(request.path_info+'?page=', page_index, data_count//24 + 1)
    page_str = page.page_str()
    carousel_list =page.video_page(data_list,24)
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
        carousel_data['vod_name'] = request.POST.get('vod_name')
        carousel_data['vod_pic'] = request.POST.get('vod_pic')
        carousel_data['vod_url'] = request.POST.get('vod_url')
        carousel_data['vod_index'] = request.POST.get('vod_index')
        # print(carousel_data)
        flag = dump_carousel_data(carousel_data)
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
        vod_name = request.POST.get('vod_name')
        del_carousel_data(vod_name)
        print("已成功添加轮播图： %s !" % vod_name)
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = e
    finally:
        return HttpResponse(json.dumps(ret))