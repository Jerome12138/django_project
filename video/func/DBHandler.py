from video import models
import json
from django.db.models import Q
import redis

# 创建StrictRedis对象，与redis服务器建⽴连接
SR = redis.StrictRedis(host='42.193.179.124', port=6372, db=0, password='jerome3201862')

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

def load_vod_data_without_douban_id():    # 从数据库获取无豆瓣id的影片数据
    result = models.VideoData.objects.filter(vod_douban_id__isnull=True).exclude(vod_cid__in=[16, 17]).values(
        'vod_id', 'vod_pic', 'vod_name', 'vod_continu', 'vod_actor', 'vod_rating', 'vod_douban_id', 'vod_year').order_by('-ctime')
    return result

def load_all_vod_data():    # 从数据库获取全部影片数据
    result = models.VideoData.objects.exclude(vod_cid__in=[16, 17]).values(
        'vod_id', 'vod_pic', 'vod_name', 'vod_continu', 'vod_actor', 'vod_rating', 'vod_douban_id', 'vod_year').order_by('-ctime')
    return result


def dump_request_data(request_data):  # 将视频数据保存至请求数据库
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
        'vod_id', 'vod_pic', 'vod_name', 'vod_year', 'vod_continu', 'vod_actor', 'vod_douban_id', 'vod_rating'
        ).order_by('-vod_year','-ctime')
    return result

def search_data2(wd,year):  # 从数据库按关键字搜索
    if year:
        result = models.VideoData.objects.filter(vod_name__icontains=wd).filter(vod_year=year).exclude(vod_cid__in=[16, 17]).all()
    else:
        result = models.VideoData.objects.filter(vod_name__icontains=wd).exclude(vod_cid__in=[16, 17]).all()
    return result

def load_type_data(**filter_param):  # 从数据库查询视频分类数据
    if filter_param['vod_cid'] == '1':  # 所有电影
        filter_param['vod_cid__in'] = [
            '1', '5', '6', '7', '8', '9', '10', '11']
        filter_param.pop('vod_cid')
    elif filter_param['vod_cid'] == '2':  # 所有电视剧
        filter_param['vod_cid__in'] = [
            '2', '12', '13', '14', '15', '19', '20', '21', '22']
        filter_param.pop('vod_cid')
    # 2010年以前
    if filter_param.get('vod_year') == '更早':
        filter_param['vod_year__lt'] = '2010'
        filter_param.pop('vod_year')
    # 其他地区
    if filter_param.get('vod_area') == '其他':
        filter_param['vod_area__in'] = ['新加坡', '马来西亚', '俄罗斯', '英国', '其他', '']
        filter_param.pop('vod_area')
    if filter_param.get('vod_rating') is not None:
        rating = filter_param.pop('vod_rating')
        if rating.endswith('以下'):
            filter_param['vod_rating__lt'] = '5'
        elif rating =='9.0':
            filter_param['vod_rating__gte'] = rating
        else:
            filter_param['vod_rating__gte'] = rating
            filter_param['vod_rating__lt'] = float(rating)+1
    if filter_param.get('no_rating'):
        filter_param.pop('no_rating')
        filter_param['vod_rating'] = None
    if filter_param.get('no_douban_id'):
        filter_param.pop('no_douban_id')
        filter_param['vod_douban_id'] = None
    result = models.VideoData.objects.filter(**filter_param).all().values(
        'vod_id', 'vod_pic', 'vod_name', 'vod_continu', 'vod_actor', 'vod_rating', 'vod_douban_id', 'vod_year'
        ).order_by('-vod_year','-ctime')
    return result


def load_log(log_path):  # 日志
    with open(log_path, 'r', encoding="utf-8") as f:
        log = f.read()
    return log


def dump_bulk_data(data_list):    # 将视频数据保存至数据库url1
    try:
        obj_list = []
        update_list = []
        for item in data_list:
            add_list = ['vod_id', 'vod_cid', 'vod_name', 'vod_actor', 'vod_director', 'vod_content', 'vod_pic',
                        'vod_area', 'vod_language', 'vod_year', 'vod_addtime', 'vod_url', 'vod_length', 'vod_continu', 'list_name']
            new_item = {}
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
            new_item = {}
            for i in add_list:
                new_item[i] = item[i]
            new_item['vod_url2'] = new_item.pop('vod_url')
            # 如果视频名称、年份、导演一致则判断为重复视频
            vod_obj = models.VideoData.objects.filter(
                vod_name=item['vod_name'], vod_year=item['vod_year'], vod_director=item['vod_director']).exclude(vod_url=None).first()
            # 添加进对应列表
            if vod_obj:  # url1存在，更新url2
                new_item['vod_id'] = vod_obj.vod_id
                new_obj = models.VideoData(**new_item)
                update_url2_list.append(new_obj)
                # print(new_obj.vod_name)
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


def clear_url2():
    # models.VideoData.objects.filter(vod_url2='1').update(vod_url2=None)
    pass


def clear_url():
    # models.VideoData.objects.filter(vod_url=None).delete()
    pass


def get_none_rating():  # 获取有豆瓣id，但是豆瓣评分为None，False或者为0
    result = models.VideoData.objects.exclude(vod_douban_id=None).filter(Q(vod_rating=None)|Q(vod_rating=False)|Q(vod_rating=0)).all().values(
        'vod_id', 'vod_pic', 'vod_name', 'vod_continu', 'vod_actor', 'vod_rating', 'vod_douban_id', 'vod_year'
        ).order_by('-vod_year','-ctime')
    return result

def dump_carousel_data(carousel_data):  # 将视频数据保存至请求数据库
    try:
        if carousel_data.get('vod_id'):
            obj = models.CarouselList.objects.filter(
                id=carousel_data['vod_id']).first()
            obj.__dict__.update(carousel_data)
            obj.save()
            print('数据已更新:%s' % carousel_data['vod_name'])
        else:
            models.CarouselList.objects.create(**carousel_data)
            print('数据已添加：%s' % carousel_data['vod_name'])
        return True
    except Exception as e:
        print(e)
        return False


def load_carousel_data():  # 从数据库获取数据
    result = models.CarouselList.objects.all().values().order_by('vod_index')
    return result


def del_carousel_data(vod_id):  # 从数据库删除数据
    result = models.CarouselList.objects.filter(id=vod_id).delete()
    return result


def dump_douban_id(vod_id, douban_id):
    models.VideoData.objects.filter(
        vod_id=vod_id).update(vod_douban_id=douban_id)


def dump_rating(vod_id, rating):
    models.VideoData.objects.filter(vod_id=vod_id).update(vod_rating=rating)


def redis_dump(skey, sdata):
    try:
        SR.set(skey, sdata)
        return True
    except Exception as e:
        print('redis_dump exception:', e)
        return False


def redis_load(skey):
    try:
        result = SR.get(skey)
        return result
    except Exception as e:
        print('redis_load exception:', e)
        return []

def redis_dumplist(skey, data_list):
    try:
        exist_list = SR.lrange(skey, 0, -1)
        data_list = list(set(data_list)-set(exist_list))    # 差集，已存在则不添加
        if len(data_list)>0:
            result = SR.rpush(skey, *data_list)
        return True
    except Exception as e:
        print('redis_dumplist exception:', e)
        return False


def redis_loadlist(skey):
    try:
        result = SR.lrange(skey, 0, -1)
        # result = SR.get(skey)
        # result = [item.decode() for item in result]
        # s2 = SR.keys()
        # print(result)
        return result
    except Exception as e:
        print('redis_load exception:', e)
        return []


def db_test():
    try:
        l_len = SR.llen('douban_none_list')
        l_list = SR.lrange('douban_none_list', 0, -1)
        print(l_len)
        # print(SR.lrange('douban_none_list', 0, -1))
        # return SR.lrange('douban_none_list', 0, -1)
        j=0
        for i in set(l_list):
            if l_list.count(i)>1:
                SR.lrem('douban_none_list', 1-l_list.count(i), i)
                # SR.rpush('douban_none_list', i)
                j+=1
                print(j)
        result = True
    except Exception as e:
        print('db_test exception:', e)
        result = False
    return result