from django.shortcuts import render, redirect, HttpResponse
from django.http.response import JsonResponse

from video import models
from .func.GetPageData import get_data_list, IQiyi
from .func import DBHandler
from .func.pagination import Page
import time
import json
import os

# Create your views here.


def home(request):  # 主页
    movie_list = DBHandler.load_type_data(**{'vod_cid':'1','vod_year':'2020'})
    ju_list = DBHandler.load_type_data(**{'vod_cid':'2','vod_year':'2020'})
    show_list = DBHandler.load_type_data(**{'vod_cid':'3','vod_year':'2020'})
    animation_list = DBHandler.load_type_data(**{'vod_cid':'4','vod_year':'2020'})
    # 轮播图
    carousel_list = DBHandler.load_carousel_data()
    return render(request, 'video_home.html', {
        "carousel_list":carousel_list,
        "movie_list": movie_list[0:12],
        "ju_list": ju_list[0:12],
        "show_list": show_list[0:12],
        "animation_list": animation_list[0:12],
        'all_type_id': '0'
    })


def vod_type(request, vod_cid):  # 视频分类页
    # 筛选项处理
    area = request.GET.get('area')
    year = request.GET.get('year')
    rating = request.GET.get('rating')
    filter_param = {'vod_cid': vod_cid} # 筛选参数集，查询数据库时使用
    filter_flag = False
    if area:
        filter_param['vod_area'] = area
    if year:
        filter_param['vod_year'] = year
    if rating:
        filter_param['vod_rating'] = rating
    # filter_dict 筛选参数，用于前端筛选
    filter_dict = {
        'type': [], 'area': [],
        'year': ['2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010', '更早'],
        'rating':['9.0','8.0','7.0','6.0','5.0','5.0以下']}
    if vod_cid in ['1', '5', '6', '7', '8', '9', '10', '11']:
        all_type_id = '1'
        filter_flag = True
        filter_dict['type'] = [
            {'cid': '5', 'cname': '动作片'}, {'cid': '6',
                                           'cname': '喜剧片'}, {'cid': '8', 'cname': '科幻片'},
            {'cid': '7', 'cname': '爱情片'}, {'cid': '9', 'cname': '恐怖片'}, {
                'cid': '11', 'cname': '战争片'},
            {'cid': '10', 'cname': '剧情片'}]
        filter_dict['area'] = ['大陆', '香港', '美国', '台湾', '英国',
                               '韩国', '日本', '西班牙', '法国', '印度', '加拿大', '泰国', '其它']
    elif vod_cid in ['2', '12', '13', '14', '15', '19', '20', '21', '22']:
        all_type_id = '2'
        filter_dict['type'] = [
            {'cid': '12', 'cname': '国产剧'}, {'cid': '13',
                                            'cname': '香港剧'}, {'cid': '15', 'cname': '欧美剧'},
            {'cid': '14', 'cname': '韩国剧'}, {'cid': '19',
                                            'cname': '台湾剧'}, {'cid': '20', 'cname': '日本剧'},
            {'cid': '21', 'cname': '海外剧'}, {'cid': '22', 'cname': '记录片'}]
        filter_dict['area'] = ['大陆', '香港', '美国',
                               '台湾', '英国', '韩国', '日本', '加拿大', '泰国', '其它']
    else:
        filter_dict['area'] = ['大陆', '香港', '美国', '台湾', '韩国', '日本', '其它']
        all_type_id = vod_cid
    # 查询数据
    data_list = DBHandler.load_type_data(**filter_param)
    data_count = len(data_list)
    # 分页处理
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    url_str = request.path_info+'?'
    if area:
        url_str += '&area=%s' % area
    if year:
        url_str += '&year=%s' % year
    page = Page(url_str+'&page=', page_index, data_count//24 + 1)
    page_str = page.page_str()
    video_list = page.video_page(data_list, 24)
    if video_list == -1:
        return HttpResponse('请求错误')
    return render(request, 'video_type.html', {
        "video_list": video_list,
        'page_str': page_str,
        "data_count": data_count,
        'all_type_id': all_type_id,
        'filter_param': filter_param,
        'filter_flag': filter_flag,
        'filter_dict': filter_dict,
    })


def play(request, vod_id, url_index=1, index=1):  # 播放页面
    vod_data = DBHandler.load_vod_data(vod_id)
    if not vod_data:
        return render(request, 'video_nonepage.html', {'msg': "影片尚未收录,有需要请联系管理员"})
    # url1
    url = vod_data.vod_url
    if url and len(url.split('$')) <= 2:  # 如果url只有一个，则转换为列表
        if url[0:1] != '[':
            url_list = [url, ]
        else:
            url_list = eval(url)
    elif url:
        if '\r\n' in url:
            url_list = url.split('\r\n')
        else:
            url_list = eval(url)
    else:
        url_list = []
    video_list = [item.split('$') for item in url_list]
    # url2
    url2 = vod_data.vod_url2
    # print(url2,type(url2))
    if url2 and len(url2.split('$')) <= 2:  # 如果url只有一个，则转换为列表
        if url2[0:1] != '[':    # 不是列表形式，转换为列表
            url2_list = [url2, ]
        else:   # 列表形式
            url2_list = eval(url2)
    elif url2:
        if '\r\n' in url2:
            url2_list = url2.split('\r\n')
        else:
            url2_list = eval(url2)
    else:
        url2_list = []
    video2_list = [item.split('$') for item in url2_list]
    if url_index == 1:
        video_url = video_list[index-1]
    elif url_index == 2:
        video_url = video2_list[index-1]
    return render(request, 'video_play.html', {
        'vod_data': vod_data,
        "video_list": video_list,
        "video2_list": video2_list,
        "url_index": url_index,
        "index": index,
        "video_url": video_url
    })


def play2(request):  # 自定义播放页
    if request.method == "GET":
        url = request.GET.get('url')
    elif request.method == "POST":
        url = request.POST.get('url')
    return render(request, 'video_play2.html', {"video_url": url})


def search(request):  # 搜索ORM获取视频信息
    if request.method == "POST":    # 搜索方式
        wd = request.POST.get('wd')
        page_index = 1
    elif request.method == "GET":   # 翻页方式
        wd = request.GET.get('wd')
        page_index = int(request.GET.get('page'))
    data_list = DBHandler.search_data(wd)
    # print(data_list)
    data_count = len(data_list)
    page = Page(request.path_info+'?wd=%s&page=' %
                wd, page_index, data_count//24 + 1)
    page_str = page.page_str()
    video_list = page.video_page(data_list, 24)
    if video_list == -1:
        return HttpResponse('请求错误')
    return render(request, 'video_search.html', {
        "video_list": video_list,
        'page_str': page_str,
        "data_count": data_count,
        'wd': wd
    })


def search2(request):  # 搜索外源视频信息
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
        if DBHandler.load_vod_data(item['vod_id']):
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
        flag = DBHandler.dump_request_data(request_data)
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


def i_search(request):  # 爱奇艺搜索
    iqiyi = IQiyi()
    if request.method == "POST":    # 搜索方式
        wd = request.POST.get('wd')
        page_index = 1
    elif request.method == "GET":   # 翻页方式
        wd = request.GET.get('wd')
        page_index = int(request.GET.get('page'))
    data_list = iqiyi.i_search(wd)
    # 分页
    data_count = len(data_list)
    page = Page(request.path_info+'?wd=%s&page=' %
                wd, page_index, data_count//24 + 1)
    page_str = page.page_str()
    video_list = page.video_page(data_list, 24)
    if video_list == -1:
        return HttpResponse('请求错误')
    # end 分页
    return render(request, 'video_i_search.html', {
        "video_list": video_list,
        'page_str': page_str,
        "data_count": data_count,
        'wd': wd
    })


def i_play(request):    # 爱奇艺播放
    iqiyi = IQiyi()
    url = request.GET.get('url')
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    if url and url.endswith('?src=search'):
        data_list = iqiyi.i_album(url)
        # 分页
        data_count = len(data_list)
        page = Page(request.path_info+'?page=', page_index, data_count//24 + 1)
        page_str = page.page_str()
        video_list = page.video_page(data_list, 24)
        if video_list == -1:
            return HttpResponse('请求错误')
        # end 分页
        return render(request, 'video_i_album.html', {
            "video_list": video_list,
            'page_str': page_str,
            "data_count": data_count,
        })
    else:
        # iqiyi.i_jeixi(url)
        # return HttpResponse('test')
        # return redirect(iqiyi.i_video(url))
        video_url = "https://okjx.cc/jiexi/?url=%s" % url
        return render(request, 'video_i_play.html', {"video_url": video_url})


def jx_play(request):    # 解析播放
    url_temp = request.GET.get('url_temp') if request.GET.get(
        'url_temp') else "https://www.administrator5.com/admin.php"
    url = request.GET.get('url') if request.GET.get('url') else ""
    video_url = "%s%s" % (url_temp, url)
    return render(request, 'video_i_play.html', {"video_url": video_url})
