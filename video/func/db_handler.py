from video import models

def dump_vod_data(vod_data):    # 将视频数据保存至数据库
    try:
        obj = models.VideoData.objects.filter(vod_id = vod_data['vod_id']).first()
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


def load_vod_data(vod_id):  # 从数据库获取数据
    result = models.VideoData.objects.filter(vod_id=vod_id).first()
    return result


def dump_request_data(request_data): # 将视频数据保存至数据库
    try:
        res = models.RequestList.objects.get_or_create(**request_data)
        if not res[1]:
            print('数据已存在:%s' % request_data['vod_name'])
        else:
            print('数据已添加：%s' % request_data['vod_name'])
        return True
    except Exception as e:
        print(e)
        return False

def update_request_data(vod_id):
    models.RequestList.objects.filter(vod_id=vod_id).update(is_add=1)
    print(vod_id+'已更新!')

def load_request_data():  # 从数据库获取数据
    result = models.RequestList.objects.all().values()
    return result

def del_request_data(vod_id):  # 从数据库获取数据
    result = models.RequestList.objects.filter(vod_id=vod_id).delete()
    return result

def load_type_data(vod_cid):  # 从数据库查询视频分类数据
    if vod_cid =='1':
        result = models.VideoData.objects.filter(vod_cid__in=['1','5','6','7','8','9','10','11','22']).all().values('vod_id', 'vod_pic', 'vod_name', 'vod_continu')
    elif vod_cid =='2':
        result = models.VideoData.objects.filter(vod_cid__in=['2','12','13','14','15','19','20','21']).all().values('vod_id', 'vod_pic', 'vod_name', 'vod_continu')
    else:
        result = models.VideoData.objects.filter(vod_cid=vod_cid).all().values('vod_id', 'vod_pic', 'vod_name', 'vod_continu')
    return result

def load_log():
    with open('uwsgi.log','r',encoding="utf-8") as f:
        log = f.read()
    return log