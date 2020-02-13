import json
import requests
from lxml import etree
from queue import Queue
import threading
from .db_handler import dump_bulk_data


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


def get_data_list(wd, page_index=1):    # 获取列表
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

def run_forever(func):  # 无限循环运行
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper



class getAllData(object):   # 获取所有数据
    def __init__(self):
        self.url_temp = "http://www.zdziyuan.com/inc/s_feifei3zuidam3u8/?p=%s"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.url_queue = Queue()
        self.page_queue = Queue()
        self.error_pages = []

    def parse_url(self, url):  # 发送请求，获取响应
        i = 0
        while i < 5:
            try:
                response = requests.get(
                    url, headers=self.headers, timeout=(3, 10))
                if response.status_code != 200:
                    print(response.status_code)
                    break
                res_dict = json.loads(response.content.decode())
                return res_dict
            except requests.exceptions.RequestException:
                i += 1
                print('page%s请求超时，重试%s' % (url.split('?p=')[1],i))
            except json.decoder.JSONDecodeError:
                print('page%s请求数据为空，已添加至错误列表'%url.split('?p=')[1])
                self.error_pages.append(url)
        return False

    def get_first_page(self):   # 获取首页数据
        # 1.设置起始url
        start_page = 1
        start_url = self.url_temp % start_page
        # 2.发送请求，获取响应
        res_dict = self.parse_url(start_url)
        if not res_dict:
            print('请求错误')
            return False
        # 4.保存数据
        page_count = int(res_dict['page']['pagecount'])
        print('一共%s页数据' % page_count)
        flag = dump_bulk_data(res_dict['data'])
        if not flag:
            print('保存出现错误,已放入错误列表')
            self.error_pages.append(start_page)
        else:
            print('保存成功')
        return page_count

    def add_url_to_queue(self, page_count): # 添加url队列
        for i in range(2, page_count+1):
            self.url_queue.put(self.url_temp % i)

    @run_forever
    def add_page_to_queue(self):    # 解析页面，添加至页面数据队列
        url = self.url_queue.get()
        res_dict = self.parse_url(url)
        if not res_dict:
            print('page:', url.split('?p=')[1], '请求出现错误，放入错误列表')
            # self.url_queue.put(url)
            self.error_pages.append(url.split('?p=')[1])
        else:
            print('获取到page:', url.split('?p=')[1])
            self.page_queue.put(res_dict)
        self.url_queue.task_done()

    @run_forever
    def save_data(self):    # 保存数据至数据库
        res_dict = self.page_queue.get()
        flag = dump_bulk_data(res_dict['data'])
        if not flag:
            print('%s保存出现错误'% res_dict['page']['pageindex'])
            self.page_queue.put(res_dict)
        else:
            print('page%s保存成功'% res_dict['page']['pageindex'])
        self.page_queue.task_done()

    def run_use_more_thread(self, func, count=1):   # 运行多线程
        for i in range(count):
            t = threading.Thread(target=func)
            t.setDaemon(True)
            t.start()

    def run(self):  # 实现主要逻辑
        # 获取首页数据
        page_count = self.get_first_page()
        if not page_count:
            return False
        elif page_count == 1:
            print('数据更新完成')
        else:
            # 获取下页数据
            self.add_url_to_queue(page_count)
            self.run_use_more_thread(self.add_page_to_queue, 30)
            self.run_use_more_thread(self.save_data, 10)
            # 等待线程结束
            self.url_queue.join()
            self.page_queue.join()
            print('数据更新完成')
            print(self.error_pages)
        return True
