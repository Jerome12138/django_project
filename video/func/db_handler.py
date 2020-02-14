from video import models

def dump_vod_data(vod_data):    # 将视频数据保存至数据库
    try:
        obj = models.VideoData.objects.filter(
            vod_id=vod_data['vod_id']).first()
        if obj:
            obj.__dict__.update(vod_data)
            obj.save()
            print('数据已更新:%s' % vod_data['vod_name'])
        else:
            models.VideoData.objects.create(**vod_data)
            print('数据已添加：%s' % vod_data['vod_name'])
        return True
    except Exception as e:
        print(e)
        return False


def load_vod_data(vod_id):  # 从数据库获取某影片数据
    result = models.VideoData.objects.filter(vod_id=vod_id).first()
    return result


def load_all_vod_data():    # 从数据库获取全部影片数据
    result = models.VideoData.objects.exclude(vod_cid__in=[16, 17]).values(
        'vod_id', 'vod_pic', 'vod_name', 'vod_continu', 'vod_actor').order_by('-ctime')
    return result


def dump_request_data(request_data):  # 将视频数据保存至数据库
    try:
        res = models.RequestList.objects.get_or_create(**request_data)
        if not res[1]:
            print('请求已存在:%s' % request_data['vod_name'])
        else:
            print('请求已添加：%s' % request_data['vod_name'])
        return True
    except Exception as e:
        print(e)
        return False


def update_request_data(vod_id):    # 更新请求数据
    models.RequestList.objects.filter(vod_id=vod_id).update(is_add=1)


def load_request_data():  # 从数据库获取数据
    result = models.RequestList.objects.all().values()
    return result


def del_request_data(vod_id):  # 从数据库获取数据
    result = models.RequestList.objects.filter(vod_id=vod_id).delete()
    return result


def load_type_data(vod_cid):  # 从数据库查询视频分类数据
    if vod_cid == '1':
        result = models.VideoData.objects.filter(vod_cid__in=['1', '5', '6', '7', '8', '9', '10', '11', '22']).all(
        ).values('vod_id', 'vod_pic', 'vod_name', 'vod_continu', 'vod_actor').order_by('-ctime')
    elif vod_cid == '2':
        result = models.VideoData.objects.filter(vod_cid__in=['2', '12', '13', '14', '15', '19', '20', '21']).all(
        ).values('vod_id', 'vod_pic', 'vod_name', 'vod_continu', 'vod_actor').order_by('-ctime')
    else:
        result = models.VideoData.objects.filter(vod_cid=vod_cid).all().values(
            'vod_id', 'vod_pic', 'vod_name', 'vod_continu', 'vod_actor').order_by('-ctime')
    return result


def load_log(log_path):  # 日志
    with open(log_path, 'r', encoding="utf-8") as f:
        log = f.read()
    return log


def dump_bulk_data(data_list):    # 将视频数据保存至数据库
    try:
        obj_list = []
        update_list = []
        for item in data_list:
            item.pop('vod_title')
            item.pop('vod_type')
            item.pop('vod_keywords')
            item.pop('vod_filmtime')
            item.pop('vod_server')
            item.pop('vod_play')
            item.pop('vod_inputer')
            item.pop('vod_reurl')
            item.pop('vod_weekday')
            item.pop('vod_copyright')
            item.pop('vod_state')
            item.pop('vod_version')
            item.pop('vod_tv')
            item.pop('vod_total')
            item.pop('vod_status')
            item.pop('vod_stars')
            item.pop('vod_hits')
            item.pop('vod_isend')
            item.pop('vod_douban_id')
            item.pop('vod_series')
            item['vod_alias'] = ""
            if not models.VideoData.objects.filter(vod_id=item['vod_id']).exists():
                obj_list.append(models.VideoData(**item))
                # models.VideoData.objects.create(**item)
            else:
                update_list.append(models.VideoData(**item))
                # obj.__dict__.update(item)
                # obj.save()
        if not obj_list:
            models.VideoData.objects.bulk_create(obj_list)
        if not update_list:
            models.VideoData.objects.bulk_update(update_list, fields=["vod_id"],batch_size=100)
        return True
    except Exception as e:
        print("保存出错：%s" % e)
        return False
