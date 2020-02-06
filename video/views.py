from django.shortcuts import render, redirect, HttpResponse

from video import models
from .func.GetPageData import *
from .func.db_handler import *
from .func.pagination import Page

# Create your views here.


def home(request):  # 主页
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = models.VideoData.objects.all().values(
        'vod_id', 'vod_pic', 'vod_name', 'vod_continu').order_by('-ctime')
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
    video_list = [item.split('$') for item in eval(vod_data.vod_url)]
    # print(video_list)
    return render(request, 'video_play.html', {
        'vod_data': vod_data,
        "video_list": video_list,
        "index": index,
        "video_url": video_list[index-1]
    })


def search(request):  # 搜索视频信息
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
    page = Page('/video/search/?wd=%s&page=' %
                wd, page_index, data_count//50 + 1)
    page_str = page.page_str()
    return render(request, 'video_search.html', {
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
        flag = dump_request_data(request_data)
        if flag:
            ret['data'] = "已成功添加 %s !" % request_data['vod_name']
        else:
            ret['status'] = False
            ret['error'] = "数据库操作出现错误"
        # print(request_data)
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


def play2(request, index=1):
    video_list = [
        "http://hong.tianzhen-zuida.com/20200101/17589_a77ac9a0/index.m3u8",
        "http://hong.tianzhen-zuida.com/20200101/17588_3b2a1b68/index.m3u8",
        "http://hong.tianzhen-zuida.com/20200102/17660_deee4d08/index.m3u8",
        "http://hong.tianzhen-zuida.com/20200102/17659_772db27f/index.m3u8",
        "http://hong.tianzhen-zuida.com/20200108/18057_a40df9d5/index.m3u8",
        "http://hong.tianzhen-zuida.com/20200108/18056_3bf27619/index.m3u8",
        "http://hong.tianzhen-zuida.com/20200109/18172_925562fc/index.m3u8",
        "http://hong.tianzhen-zuida.com/20200109/18171_35ccef5b/index.m3u8",
        "http://mei.huazuida.com/20200115/22516_26db2881/index.m3u8",
        "http://mei.huazuida.com/20200115/22515_e7f7f0f7/index.m3u8",
        "http://hong.tianzhen-zuida.com/20200116/18670_f706a37c/index.m3u8",
        "http://hong.tianzhen-zuida.com/20200116/18669_0bf2cf64/index.m3u8",
    ]
    return render(request, 'video_play2.html', {"video_count": range(len(video_list)), "index": index, "video_url": video_list[index]})


def add_vod(request):   # 添加视频数据
    ret = {'status': True, 'error': None, 'data': None}
    try:
        vod_id = request.POST.get('vod_id')
        print(vod_id)
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


def view_log(request):
    log = load_log()
    return render(request, 'video_log.html', {
        "log": log
    })