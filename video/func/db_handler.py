from video import models
import json


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


def search_data(wd):  # 从数据库按关键字搜索
    result = models.VideoData.objects.filter(vod_name__icontains=wd).exclude(vod_cid__in=[16, 17]).all().values(
        'vod_id', 'vod_pic', 'vod_name', 'vod_continu', 'vod_actor').order_by('-ctime')
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
            add_list = ['vod_id', 'vod_cid', 'vod_name', 'vod_actor', 'vod_director', 'vod_content', 'vod_pic',
                        'vod_area', 'vod_language', 'vod_year', 'vod_addtime', 'vod_url', 'vod_length', 'vod_continu', 'list_name']
            new_item={}
            for i in add_list:
                new_item[i] = item[i]
            if not models.VideoData.objects.filter(vod_id=new_item['vod_id']).exists():
                obj_list.append(models.VideoData(**new_item))
            else:
                update_list.append(models.VideoData(**new_item))
        if obj_list != []:
            models.VideoData.objects.bulk_create(obj_list)
        if update_list != []:
            models.VideoData.objects.bulk_update(
                update_list, fields=["vod_addtime", 'vod_url', 'vod_continu'], batch_size=100)
        return True
    except Exception as e:
        print("保存出错：%s" % e)
        return False

def dump_bulk_data_url2(data_list):    # 将视频数据保存至数据库url2
    try:
        obj_list = []
        update_list = []
        update_url2_list = []
        for item in data_list:
            add_list = ['vod_id', 'vod_cid', 'vod_name', 'vod_actor', 'vod_director', 'vod_content', 'vod_pic',
                        'vod_area', 'vod_language', 'vod_year', 'vod_addtime', 'vod_url', 'vod_length', 'vod_continu', 'list_name']
            new_item={}
            for i in add_list:
                new_item[i] = item[i]
            new_item['vod_url2'] = new_item.pop('vod_url')
            vod_obj = models.VideoData.objects.filter(
                vod_name=item['vod_name'],vod_year=item['vod_year'],vod_director=item['vod_director']).exclude(vod_url=None).first()
            # 添加进对应列表
            if vod_obj: # url1存在，更新url2
                new_item['vod_id']= vod_obj.vod_id
                new_obj = models.VideoData(**new_item)
                update_url2_list.append(new_obj)
            # elif not models.VideoData.objects.filter(vod_id=new_item['vod_id']).exists():# url1不存在，添加
            #     # if new_item['vod_cid'] = 
            #     pass
            #     obj_list.append(models.VideoData(**new_item))
            # else:   # url1不存在，更新url2及相关信息
            #     update_list.append(models.VideoData(**new_item))
        # if obj_list != []:
        #     models.VideoData.objects.bulk_create(obj_list)
        # if update_list != []:
        #     models.VideoData.objects.bulk_update(
        #         update_list, fields=["vod_addtime", 'vod_url2', 'vod_continu'], batch_size=100)
        if update_url2_list != []:
            models.VideoData.objects.bulk_update(
                update_url2_list, fields=['vod_url2'], batch_size=100)
        return True
    except Exception as e:
        print("保存出错：%s" % e)
        return False
