import json
import requests
from lxml import etree


class GetPage(object):  # 爬取网页数据，返回html数据
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }

    def get(self, url,*args, **kwargs):  # 获取html的xpath对象
        # 2.发送请求，获取响应
        res = requests.get(url, headers=self.headers)
        assert res.status_code == 200
        # with open('abc.html','wb') as f:
        #     f.write(res.content)
        html_str = res.content.decode(encoding='GB2312')
        # 3.提取数据
        html = etree.HTML(html_str)
        # 4.保存数据
        return html

    def post(self,url, *args, **kwargs):  # 获取html的xpath对象
        # 1.设置起始url
        # 2.发送请求，获取响应
        res = requests.post(url, headers=self.headers,
                            data=kwargs)
        assert res.status_code == 200
        html_str = res.content.decode()
        # 3.提取数据
        html = etree.HTML(html_str)
        # 4.保存数据
        return html

    def get_json_data(self,url):    # 获取json数据
        # 2.发送请求，获取响应
        res = requests.get(url, headers=self.headers)
        assert res.status_code == 200
        json_str = res.content.decode('UTF-8-sig')
        # 3.提取数据
        # ret_dict = json.loads(json_str)
        ret_dict = eval(json_str)
        return ret_dict

    def get_dict_data(self,url):    # 获取dict数据
        # 2.发送请求，获取响应
        res = requests.get(url, headers=self.headers)
        assert res.status_code == 200
        json_str = res.content.decode('UTF-8-sig')
        # 3.提取数据
        ret_dict = eval(json_str)
        # print(ret_dict)
        return ret_dict
