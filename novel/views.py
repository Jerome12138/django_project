from django.shortcuts import render, HttpResponse
from .func.db_handler import *
from .func.GetPage import *
from django.utils.safestring import mark_safe
import re

# Create your views here.


def home(request):
    return render(request, 'novel_home.html')


def get_json_data(url):
    get_page = GetPage()
    res_dict = get_page.get_json_data(url)
    assert res_dict['info'] == 'success'
    return res_dict['data']


def search(request):
    wd = request.GET.get('wd')
    if wd == '':
        wd = ' '
    url = "https://sou.jiaston.com/search.aspx?key=%s&siteid=app2" % wd
    book_list = get_json_data(url)
    return render(request, 'novel_search.html', {'book_list': book_list, 'wd': wd})


def category(request, a_id):
    url = 'https://iosapp.canrike.com/book/%s/' % a_id
    data = get_json_data(url)
    book_name = data['name']
    cate_list = data['list']
    return render(request, 'novel_category.html', {'cate_list': cate_list, 'book_name': book_name, 'a_id': a_id})


def chapter(request, a_id, c_id=-1):
    if c_id == -1:
        cate_url = 'https://iosapp.canrike.com/book/%s/' % a_id
        cate_data = get_json_data(cate_url)
        c_id = cate_data['list'][0]['list'][0]['id']
    url = 'https://iosapp.canrike.com/book/%s/%s.html' % (a_id, c_id)
    data = get_json_data(url)
    content = data['content'].replace('\r\n', '</br>')
    content = re.sub(r'</br>\s*</br>','</br>', content)
    data['content'] = mark_safe(content)
    return render(request, 'novel_chapter.html', {'art_data': data})


def get_book_text(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        a_id = request.POST.get('a_id')
        c_id = request.POST.get('c_id')
        url = 'https://iosapp.canrike.com/book/%s/%s.html' % (a_id, c_id)
        data = get_json_data(url)
        content = data['content'].replace('\r\n', '</br>')
        content = re.sub(r'</br>\s*</br>','</br>', content)
        data['content'] = mark_safe(content)
        ret['data'] = data
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = "未知错误"
    finally:
        return HttpResponse(json.dumps(ret))
