# db_handler


def load_tv_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def add_vod_to_tv(json_path,vod_id):
    with open(json_path, 'r', encoding='utf-8') as f:
        tv_json = json.load(f)
        # tv_json = {"live":[],"type":[]}
        vod_data = load_vod_data(vod_id)
        if not vod_data:
            return False
        # 处理url列表
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
        # 如果之前已存在，先删除
        for item in tv_json['type']:
            if item['id'] == vod_id:
                tv_json['type'].remove(item)
        for item in tv_json['live']:
            if item['itemid'] == vod_id:
                tv_json['live'].remove(item)
        # 添加进json
        tv_json['type'].append(
            {"id": vod_id, "name": vod_data.vod_name})
        i = 0
        for item in video_list:
            tv_json['live'].append({"num": '%s_%s' % (
                vod_id, i), "itemid": vod_id, "name": item[0], "urllist": item[1]})
            i += 1
        # print(tv_json)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(tv_json,f)
    return True

def del_vod_to_tv(json_path,vod_id):
    with open(json_path, 'r', encoding='utf-8') as f:
        tv_json = json.load(f)
        for item in tv_json['type']:
            if item['id'] == vod_id:
                tv_json['type'].remove(item)
        for item in tv_json['live']:
            if item['itemid'] == vod_id:
                tv_json['live'].remove(item)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(tv_json,f)


def tv(request):     # 管理页面
    page_index = int(request.GET.get('page')) if request.GET.get('page') else 1
    data_list = load_tv_json('video/repository/tv.json')['type']
    data_count = len(data_list)
    page = Page('/video/admin/tv/?page=', page_index, data_count//24 + 1)
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
    return render(request, 'video_tv.html', {
        "request_list": request_list,
        'page_str': page_str,
        "data_count": data_count
    })


def tv_json(request):
    ret = {'status': True, 'error': None, 'data': None}
    try:
        add_vid = request.POST.get('add_vid')
        del_vid = request.POST.get('del_vid')
        if add_vid:
            flag = add_vod_to_tv('video/repository/tv.json',add_vid)
            if not flag:
                ret['status'] = False
                ret['error'] = "视频不存在"
        elif del_vid:
            del_vod_to_tv('video/repository/tv.json',del_vid)
    except Exception as e:
        print(e)
        ret['status'] = False
        ret['error'] = "未知错误"
    finally:
        return HttpResponse(json.dumps(ret))


def tv_api(request):
    tv_json = load_tv_json('video/repository/tv.json')
    return JsonResponse(tv_json)