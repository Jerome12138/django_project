import json
import requests
from lxml import etree


class GetPageData(object):  # 爬取网页数据，返回html数据
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
        }

    def get(self, *args, **kwargs):  # 实现主要逻辑
        # 2.发送请求，获取响应
        res = requests.get(self.url, headers=self.headers)
        assert res.status_code == 200
        html_str = res.content.decode()
        # 3.提取数据
        html = etree.HTML(html_str)
        # 4.保存数据
        return html

    def post(self, *args, **kwargs):  # 实现主要逻辑
        # 1.设置起始url
        # 2.发送请求，获取响应
        res = requests.post(self.url, headers=self.headers,
                            data=kwargs)
        assert res.status_code == 200
        html_str = res.content.decode()
        # with open('abc.html','w',encoding="utf-8") as f:
        #     f.write(html_str)
        # 3.提取数据
        html = etree.HTML(html_str)
        # 4.保存数据
        return html

    def get_json_data(self):
        # 2.发送请求，获取响应
        json_str = requests.get(
            self.url, headers=self.headers).content.decode()
        # 3.提取数据
        ret_dict = json.loads(json_str)
        if ret_dict['status'] != 200:
            print(ret_dict)
            print('AssertionError')
            assert ret_dict['status'] == 200
        return ret_dict


def get_vod_data(vod_id):   # 根据vod_id爬取数据，返回数据字典
    # 1.获取数据
    url = "http://www.zuidazy2.com/?m=vod-detail-id-%s.html" % vod_id
    get_page_data = GetPageData(url)
    html = get_page_data.get()
    # 2.转化数据
    data = {}
    data['vod_id'] = vod_id
    data['vod_cid'] = html.xpath(
        '//div[@class="nvc"]/dl/dd/a[2]/@href')[0].split('vod-type-id-')[1].split('.html')[0]
    data['vod_pic'] = html.xpath('//div[@class="vodImg"]/img/@src')[0]
    data['vod_name'] = html.xpath(
        '//div[@class="vodInfo"]/div[@class="vodh"]/h2//text()')[0]
    data['vod_continu'] = html.xpath(
        '//div[@class="vodInfo"]/div[@class="vodh"]/span//text()')[0]
    vod_ul = html.xpath(
        '//div[@class="vodInfo"]/div[@class="vodinfobox"]/ul/.')[0]
    data['vod_alias'] = vod_ul.xpath('./li[1]/span/text()')[0] if vod_ul.xpath('./li[1]/span/text()') != [] else ""
    data['vod_director'] = vod_ul.xpath('./li[2]/span/text()')[0] if vod_ul.xpath('./li[2]/span/text()') != [] else ""
    data['vod_actor'] = vod_ul.xpath('./li[3]/span/text()')[0] if vod_ul.xpath('./li[3]/span/text()') != [] else ""
    data['list_name'] = vod_ul.xpath('./li[4]/span/text()')[0]
    data['vod_area'] = vod_ul.xpath('./li[5]/span/text()')[0] if vod_ul.xpath('./li[5]/span/text()') != [] else ""
    data['vod_language'] = vod_ul.xpath('./li[6]/span/text()')[0] if vod_ul.xpath('./li[6]/span/text()') != [] else ""
    data['vod_year'] = vod_ul.xpath('./li[7]/span/text()')[0] if vod_ul.xpath('./li[7]/span/text()') != [] else ""
    data['vod_length'] = vod_ul.xpath('./li[8]/span/text()')[0] if vod_ul.xpath('./li[8]/span/text()') != [] else ""
    data['vod_addtime'] = vod_ul.xpath('./li[9]/span/text()')[0] if vod_ul.xpath('./li[9]/span/text()') != [] else ""
    data['vod_content'] = vod_ul.xpath('./li[@class="cont"]/div/span[@class="more"]/text()')[0] if vod_ul.xpath('./li[@class="cont"]/div/span[@class="more"]/text()') != [] else ""
    data['vod_url'] = html.xpath('//div[@id="play_1"]/ul/li/text()')
    # print(data)
    return(data)


def get_data_list(wd, page_index=1):
    get_page_data = GetPageData(
        "http://zuidazy2.com/index.php?m=vod-search-pg-%s-wd-%s.html" % (page_index, wd))
    html = get_page_data.get()
    data_list = html.xpath('//div[@class="xing_vb"]/ul//span[@class="tt"]/..')
    data_count = int(html.xpath(
        '//div[@class="nvc"]//dd/span[2]/text()')[0].strip())
    # print(data_count)
    video_list = []
    for i in data_list:
        try:
            temp = {
                'vod_id': i.xpath('./span[@class="xing_vb4"]/a/@href')[0].split('vod-detail-id-')[1].split('.html')[0],
                'vod_name': i.xpath('./span[@class="xing_vb4"]/a/text()')[0],
                'vod_continu': i.xpath('./span[@class="xing_vb4"]/a/span/text()')[0] if i.xpath('./span[@class="xing_vb4"]/a/span/text()') != [] else "",
                'list_name': i.xpath('./span[@class="xing_vb5"]/text()')[0],
                'vod_addtime': i.xpath('./span[@class="xing_vb6"]/text()')[0],
            }
            video_list.append(temp)
        except Exception as e:
            print(e)
            print(temp)
            print(i.xpath('./span[@class="xing_vb4"]//text()'))
    return video_list, data_count
