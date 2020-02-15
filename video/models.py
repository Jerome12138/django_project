from django.db import models


# Create your models here.
class VideoData(models.Model):
    vod_id = models.CharField(
        max_length=8, unique=True, primary_key=True)  # 视频id
    vod_cid = models.CharField(max_length=4)  # 视频分类id
    vod_name = models.CharField(max_length=16)    # "警察日记"
    vod_alias = models.CharField(max_length=16)    # 别名
    # vod_type = models.CharField(max_length=32)  # "惊悚,悬疑,剧情"
    # vod_keywords = models.CharField(max_length=32)
    vod_actor = models.CharField(max_length=32)  # "王景春,陈维涵,孙亮,侯岩松,袁利坚,白波"
    vod_director = models.CharField(max_length=32)  # "宁瀛"
    vod_content = models.TextField()  # "内蒙古鄂尔多斯市准格尔旗公安局长郝万忠英年早逝后，..."
    # "https://tu.tianzuida.com/pic/upload/vod/2020-02-04/202002041580782039.jpg"
    vod_pic = models.CharField(max_length=128)
    vod_area = models.CharField(max_length=16)  # "大陆"
    vod_language = models.CharField(max_length=16)  # "国语"
    vod_year = models.CharField(max_length=4)  # "2014"
    vod_addtime = models.CharField(max_length=32)  # "2020-02-04 10:17:47"
    # "HD1280高清国语中字版$https://meng.wuyou-zuida.com/20200203/25682_6a2d6704/index.m3u8"
    vod_url = models.TextField()
    vod_length = models.IntegerField()
    # # "http://www.zuidazy1.net/?m=vod-detail-id-78482.html"
    # vod_reurl = models.CharField(max_length=128)
    vod_continu = models.CharField(max_length=32)  # "HD1280高清国语中字版"
    # vod_status = models.IntegerField()  # 1
    # vod_isend = models.IntegerField()  # 1
    list_name = models.CharField(max_length=32)
    # video_list = models.ForeignKey(
    #     "VideoList", to_field='list_id', on_delete=models.CASCADE)  # "剧情片"
    ctime = models.DateTimeField(auto_now=True)


# class VideoList(models.Model):
#     list_id = models.CharField(max_length=4, unique=True)  # 视频分类id
#     list_name = models.CharField(max_length=16)  # "剧情片"


class RequestList(models.Model):
    vod_id = models.CharField(max_length=8, unique=True)  # 视频id
    # request_times = models.IntegerField() # 记录请求次数
    vod_name = models.CharField(max_length=16)    # "警察日记"
    list_name = models.CharField(max_length=16)  # "剧情片"
    vod_continu = models.CharField(max_length=32)
    vod_addtime = models.CharField(max_length=32)
    is_add = models.IntegerField()


'''
{list_id: 1, list_name: "电影片"}
{list_id: 5, list_name: "动作片"}
{list_id: 6, list_name: "喜剧片"}
{list_id: 7, list_name: "爱情片"}
{list_id: 8, list_name: "科幻片"}
{list_id: 9, list_name: "恐怖片"}
{list_id: 10, list_name: "剧情片"}
{list_id: 11, list_name: "战争片"}
{list_id: 22, list_name: "记录片"}

{list_id: 2, list_name: "连续剧"}
{list_id: 12, list_name: "国产剧"}
{list_id: 13, list_name: "香港剧"}
{list_id: 14, list_name: "韩国剧"}
{list_id: 15, list_name: "欧美剧"}
{list_id: 19, list_name: "台湾剧"}
{list_id: 20, list_name: "日本剧"}
{list_id: 21, list_name: "海外剧"}

{list_id: 3, list_name: "综艺片"}

{list_id: 4, list_name: "动漫片"}


{list_id: 16, list_name: "福利片"}
{list_id: 17, list_name: "伦理片"}
{list_id: 18, list_name: "音乐片"}


'''
