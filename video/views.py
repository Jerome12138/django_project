from django.shortcuts import render
import requests
import json
from lxml import etree

# Create your views here.


def home(request):
    pass
    return render(request, 'video_list.html')


def play(request):
    pass
    return render(request, 'video_play.html')


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
    return render(request, 'video_play2.html', {"video_count":range(len(video_list)),"index": index,"video_url": video_list[index]})


class GetPageData(object):
    def __init__(self):
        self.url_temp = "http://www.zdziyuan.com/inc/s_feifei3zuidam3u8/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }

    def parse_url(self, url):  # 发送请求，获取响应
        return requests.get(url, headers=self.headers).content.decode()

    def get_data(self, json_str):
        ret_dict = json.loads(json_str)
        if ret_dict['code'] != 200:
            print(ret_dict)
            print('AssertionError')
            assert ret_dict['code'] == 200
        return ret_dict

    def run(self, category1=0):  # 实现主要逻辑
        # 1.设置起始url
        start_page = 1
        start_url = self.url_temp
        # 2.发送请求，获取响应
        json_str = self.parse_url(start_url)
        # 3.提取数据
        data = self.get_data(json_str)
        page_index = int(data['page']['pageindex'])
        page_count = int(data['page']['pagecount'])
        page_size = int(data['page']['pagesize'])
        record_count = int(data['page']['recordcount'])
        # 4.保存数据
        current_page = start_page
        print('current_page:%s added' % current_page)
        item_list = data['data']['auctionInfos']
        # 5.获取下一页数据
        while data['hasNext']:
            if current_page == 40:
                break
            current_page += 1
            next_url = self.url_temp % (current_page, page_size, category1)
            json_str = self.parse_url(next_url)
            data = self.get_data(json_str)
            item_list += data['data']['auctionInfos']
            print('current_page:%s added' % current_page)
        # 6.保存文件
        return item_list
