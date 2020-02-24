from django.shortcuts import render, redirect, HttpResponse

from video import models
from .func.GetPageData import *
from .func.db_handler import *
from .func.pagination import Page
import time
import os

# Create your views here.

user_list = {}


def home(request):  # 主页
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = load_all_vod_data()
    data_count = len(data_list)
    page = Page('/video/home/?page=', page_index, data_count//24 + 1)
    page_str = page.page_str()
    if page_index < data_count//24 + 1:
        start_index = (page_index-1)*24
        end_index = page_index*24
    elif page_index == data_count//24 + 1:
        start_index = (page_index-1)*24
        end_index = data_count
    else:
        return HttpResponse('请求错误')
    video_list = data_list[start_index:end_index]
    return render(request, 'video_home.html', {
        "video_list": video_list,
        'page_str': page_str,
        "data_count": data_count
    })


def play(request, vod_id, index=1):  # 播放页面
    vod_data = load_vod_data(vod_id)
    if not vod_data:
        return render(request, 'video_nonepage.html', {'msg': "影片尚未收录,有需要请联系管理员"})
    url = vod_data.vod_url
    if len(url.split('$')) <= 2:  # 如果url只有一个，则转换为列表
        if url[0:1] != '[':
            url_list = [url, ]
        else:
            url_list = eval(url)
    else:
        if '\r\n' in url:
            url_list = url.split('\r\n')
        else:
            url_list = eval(url)
    video_list = [item.split('$') for item in url_list]
    return render(request, 'video_play.html', {
        'vod_data': vod_data,
        "video_list": video_list,
        "index": index,
        "video_url": video_list[index-1]
    })


def play2(request):
    if request.method == "GET":
        url = request.GET.get('url')
    elif request.method == "POST":
        url = request.POST.get('url')
    return render(request, 'video_play2.html', {"video_url": url})


def search(request):  # 搜索视频信息
    if request.method == "POST":    # 搜索方式
        wd = request.POST.get('wd')
        page_index = 1
    elif request.method == "GET":   # 翻页方式
        wd = request.GET.get('wd')
        page_index = int(request.GET.get('page'))
    data_list = search_data(wd)
    data_count = len(data_list)
    page = Page('/video/search/?wd=%s&page=' %
                wd, page_index, data_count//24 + 1)
    page_str = page.page_str()
    if page_index < data_count//24 + 1:
        start_index = (page_index-1)*24
        end_index = page_index*24
    elif page_index == data_count//24 + 1:
        start_index = (page_index-1)*24
        end_index = data_count
    else:
        return HttpResponse('请求错误')
    video_list = data_list[start_index:end_index]
    return render(request, 'video_search.html', {
        "video_list": video_list,
        'page_str': page_str,
        "data_count": data_count,
        'wd': wd
    })


def search2(request):  # 搜索视频信息
    if request.method == "POST":
        wd = request.POST.get('wd')
        page_index = 1
    elif request.method == "GET":
        wd = request.GET.get('wd')
        page_index = int(request.GET.get('page'))
    # print(wd, page_index)
    video_list, data_count = get_data_list(wd, page_index)
    # print(video_list)
    for item in video_list:
        if load_vod_data(item['vod_id']):
            item['is_save'] = 1
        else:
            item['is_save'] = 0
    page = Page('/video/search2/?wd=%s&page=' %
                wd, page_index, data_count//50 + 1)
    page_str = page.page_str()
    return render(request, 'video_search2.html', {
        "video_list": video_list,
        "wd": wd,
        "page_index": page_index,
        "data_count": data_count,
        'page_str': page_str
    })


def push_request(request):  # 提交请求给管理员
    ret = {'status': True, 'error': None, 'data': None}
    try:
        request_data = {}
        request_data['vod_id'] = request.POST.get('vod_id')
        request_data['vod_name'] = request.POST.get('vod_name')
        request_data['vod_addtime'] = request.POST.get('vod_addtime')
        request_data['vod_continu'] = request.POST.get('vod_continu')
        request_data['list_name'] = request.POST.get('list_name')
        request_data['is_add'] = 0
        # print(request_data)
        flag = dump_request_data(request_data)
        if flag:
            ret['data'] = "已成功添加请求： %s !" % request_data['vod_name']
        else:
            ret['status'] = False
            ret['error'] = "数据库操作出现错误"
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = "未知错误"
    finally:
        return HttpResponse(json.dumps(ret))


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


def admin(request):     # 管理页面
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = load_request_data()
    data_count = len(data_list)
    page = Page('/video/admin/?page=', page_index, data_count//24 + 1)
    page_str = page.page_str()
    if page_index < data_count//24 + 1:
        start_index = (page_index-1)*24
        end_index = page_index*24
    elif page_index == data_count//24 + 1:
        start_index = (page_index-1)*24
        end_index = data_count
    else:
        return HttpResponse('请求错误')
    request_list = data_list[start_index:end_index]
    return render(request, 'video_admin.html', {
        "request_list": request_list,
        'page_str': page_str,
        "data_count": data_count
    })


def vod_type(request, vod_cid):
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = load_type_data(vod_cid)
    data_count = len(data_list)
    page = Page('/video/type/%s/?page=' %
                vod_cid, page_index, data_count//24 + 1)
    page_str = page.page_str()
    if page_index < data_count//24 + 1:
        start_index = (page_index-1)*24
        end_index = page_index*24
    elif page_index == data_count//24 + 1:
        start_index = (page_index-1)*24
        end_index = data_count
    else:
        return HttpResponse('请求错误')
    video_list = data_list[start_index:end_index]
    return render(request, 'video_home.html', {
        "video_list": video_list,
        'page_str': page_str,
        "data_count": data_count
    })


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


def view_log(request, log_date=0):
    if log_date == 0:
        log_date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        is_today = True
        log_path = 'uwsgi.log'
    else:
        is_today = False
        log_path = 'logs/uwsgi-%s.log' % log_date
        if not(os.path.exists(log_path) and os.path.isfile(log_path)):
            return render(request, 'video_nonepage.html', {'msg': '当天无日志'})
    log = load_log(log_path)
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
    log_str = re.sub(r'(.+?\(HTTP\/1\.1\s30\d\).+\n)', '', log)
    # print(log_str)
    return render(request, 'video_log.html', {
        "log": log_str,
        'log_date': log_date,
        'is_today': is_today
    })


def update(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        get_all_data = getAllData()
        updata_count = get_all_data.run()
        ret['data'] = '已更新%s条数据' % updata_count
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = "未知错误"
    finally:
        return HttpResponse(json.dumps(ret))
