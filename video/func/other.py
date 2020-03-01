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