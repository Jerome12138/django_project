import json
import re
import time
import logging
import requests
from lxml import etree
from queue import Queue, LifoQueue
import threading
from .db_handler import dump_bulk_data, dump_bulk_data_url2

logger = logging.getLogger('log')


class GetWebData(object):  # 爬取网页数据，返回html数据
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        }

    def get_html(self, url, is_debug=0, *args, **kwargs):  # 实现主要逻辑
        if kwargs.get('referer'):
            self.headers['Referer'] = kwargs['referer']
        res = requests.get(url, headers=self.headers)
        if res.status_code == 200:
            html_str = res.content.decode()
        else:
            print('爬虫网站%s返回状态码错误：%s' % (url, res.status_code))
            return False
        if is_debug:
            with open('abc.html', 'w', encoding="utf-8") as f:
                f.write(html_str)
        html = etree.HTML(html_str)
        return html

    def get_json(self, url):
        i = 0
        while i < 3:
            try:
                response = requests.get(
                    url, headers=self.headers, timeout=(3, 15))
                if response.status_code != 200:
                    print('Status Code：', response.status_code)
                    return False
                res_json = json.loads(response.content.decode())
                return res_json
            except requests.exceptions.RequestException:
                i += 1
                print('page%s请求超时，重试%s次' % (url.split('?p=')[1], i))
            except json.decoder.JSONDecodeError:
                i += 1
                print('page%s jSON解析错误，重试%s次' % (url.split('?p=')[1],i))
        return False


def get_vod_data(vod_id):   # 根据vod_id爬取数据，返回数据字典
    # 1.获取数据
    get_web_data = GetWebData()
    html = get_web_data.get_html(
        "http://www.zuidazy2.com/?m=vod-detail-id-%s.html" % vod_id)
    if html is None:
        return False
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
    data['vod_alias'] = vod_ul.xpath(
        './li[1]/span/text()')[0] if vod_ul.xpath('./li[1]/span/text()') != [] else ""
    data['vod_director'] = vod_ul.xpath(
        './li[2]/span/text()')[0] if vod_ul.xpath('./li[2]/span/text()') != [] else ""
    data['vod_actor'] = vod_ul.xpath(
        './li[3]/span/text()')[0] if vod_ul.xpath('./li[3]/span/text()') != [] else ""
    data['list_name'] = vod_ul.xpath('./li[4]/span/text()')[0]
    data['vod_area'] = vod_ul.xpath(
        './li[5]/span/text()')[0] if vod_ul.xpath('./li[5]/span/text()') != [] else ""
    data['vod_language'] = vod_ul.xpath(
        './li[6]/span/text()')[0] if vod_ul.xpath('./li[6]/span/text()') != [] else ""
    data['vod_year'] = vod_ul.xpath(
        './li[7]/span/text()')[0] if vod_ul.xpath('./li[7]/span/text()') != [] else ""
    data['vod_length'] = vod_ul.xpath(
        './li[8]/span/text()')[0] if vod_ul.xpath('./li[8]/span/text()') != [] else ""
    data['vod_addtime'] = vod_ul.xpath(
        './li[9]/span/text()')[0] if vod_ul.xpath('./li[9]/span/text()') != [] else ""
    data['vod_content'] = vod_ul.xpath('./li[@class="cont"]/div/span[@class="more"]/text()')[
        0] if vod_ul.xpath('./li[@class="cont"]/div/span[@class="more"]/text()') != [] else ""
    data['vod_url'] = html.xpath('//div[@id="play_1"]/ul/li/text()')
    # print(data)
    return(data)


def get_data_list(wd, page_index=1):    # 获取搜索列表
    get_web_data = GetWebData()
    html = get_web_data.get_html(
        "http://zuidazy2.com/index.php?m=vod-search-pg-%s-wd-%s.html" % (page_index, wd))
    if html is None:
        return False
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
            if str(temp['list_name']) != '伦理片' and str(temp['list_name']) != '福利片':
                video_list.append(temp)
            else:
                data_count -= 1
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
    def __init__(self, url, url_index=1):
        self.url_temp = url
        self.url_index = url_index
        self.updated = 0
        self.page_size = 40
        self.get_web_data = GetWebData()
        self.url_queue = LifoQueue()
        self.page_queue = Queue()
        self.error_pages = []

    def parse_url(self, url):  # 发送请求，获取响应
        return self.get_web_data.get_json(url)

    def get_update_count(self, url_index):   # 获取今日更新数量
        try:
            # 1.匹配来源
            if url_index == 1:
                url = "http://www.zuidazy4.com/"
                x_match = "//li[contains(text(),'今日更新：')]/strong/text()"
            else:
                url = "http://bajieziyuan.com/"
                x_match = "//a[contains(string(),'今日更新：')]/font[2]/text()"
            # 2.获取数据
            get_web_data = GetWebData()
            html = get_web_data.get_html(url)
            if html is None:
                update_count = 480
            # 3.转化数据
            x_update = html.xpath(x_match)
            update_count = int(x_update[0]) if x_update != [] else 480
            print("站点%s今日更新：" % url_index, update_count)
        except Exception as e:
            print("获取更新数量出错：%s" % e)
            update_count = 480
        finally:
            return update_count

    def get_first_page(self):   # 获取首页数据
        # 1.设置起始url
        start_page = 1
        start_url = self.url_temp % start_page
        # 2.发送请求，获取响应
        res_dict = self.parse_url(start_url)
        if not res_dict:
            logger.error('首页请求无数据')
            return False
        # 4.保存数据
        page_count = int(res_dict['page']['pagecount'])
        self.page_size = int(res_dict['page']['pagesize'])
        return page_count

    def add_url_to_queue(self, page_count):  # 添加url队列
        for i in range(1, page_count+1):
            self.url_queue.put(i)

    @run_forever
    def add_page_to_queue(self):    # 解析页面，添加至页面数据队列
        url = self.url_temp % self.url_queue.get()
        res_dict = self.parse_url(url)
        if not res_dict:
            logger.error('page:', url.split('?p=')[1], '请求无数据，放入错误列表')
            # self.url_queue.put(url)
            self.error_pages.append(url.split('?p=')[1])
        else:
            if int(url.split('?p=')[1]) % 100 == 0:
                logger.console('获取到page:', url.split('?p=')[1])
            self.page_queue.put(res_dict)
        self.url_queue.task_done()

    @run_forever
    def save_data(self):    # 保存数据至数据库
        res_dict = self.page_queue.get()
        # 匹配站点
        if self.url_index == 1:
            is_saved = dump_bulk_data(res_dict['data'])
        elif self.url_index == 2:
            is_saved = dump_bulk_data_url2(res_dict['data'])
        else:
            raise Exception('url参数错误(save_data)')
        if not is_saved:
            logger.error('%s保存出现错误' % res_dict['page']['pageindex'])
            self.page_queue.put(res_dict)
        else:
            self.updated += len(res_dict['data'])
            if int(res_dict['page']['pageindex']) % 100 == 0:
                logger.console('page%s保存成功' % res_dict['page']['pageindex'])
        self.page_queue.task_done()

    def run_use_more_thread(self, func, count=1):   # 运行多线程
        for i in range(count):
            t = threading.Thread(target=func)
            t.setDaemon(True)
            t.start()

    def run(self, flag=0, up_count=-1):  # 实现主要逻辑
        print('--------%s 站点%s开始更新--------' %
              (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.url_index))
        # 获取首页数据
        update_page = self.get_first_page()
        if not update_page:
            return False
        # 获取更新数量
        if not flag:    # 更新部分数据
            page_thread = 5
            save_thread = 3
            if up_count == -1:
                update_count = self.get_update_count(self.url_index)
            else:
                update_count = up_count if up_count < 10000 else 10000
            update_page = (update_count-1)//self.page_size + 1
        else:   # 更新所有数据
            print('一共%s页数据' % page_count)
            page_thread = 30
            save_thread = 10
        if update_page:
            # 获取下页数据
            self.add_url_to_queue(update_page)
            self.run_use_more_thread(self.add_page_to_queue, page_thread)
            self.run_use_more_thread(self.save_data, save_thread)
            # 等待线程结束
            self.url_queue.join()
            self.page_queue.join()
        print('已更新%s条数据' % self.updated)
        if self.error_pages != []:
            print('出现错误页面：', self.error_pages)
        print('--------%s 站点%s更新完成--------' %
              (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), self.url_index))
        return self.updated


class IQiyi(object):  # 爱奇艺视频搜索及解析
    def __init__(self):  # 初始化
        self.get_web_data = GetWebData()

    def i_search(self, wd):  # 搜索视频
        html = self.get_web_data.get_html('https://so.iqiyi.com/so/q_'+wd)
        if html is None:
            return False
        x_vod_list = html.xpath(
            '//div[contains(@class,"qy-search-result-con")]/div[@class="layout-main"]/div[@desc="搜索列表"]/div[@desc="card"]')
        vod_list = []
        print(len(x_vod_list))
        for x_vod in x_vod_list:
            vod_dict = {}
            x_vod_type = x_vod.xpath(
                './/h3[contains(@class,"qy-search-result-tit")]//span[@class="item-type"]/text()')
            vod_dict['vod_type'] = x_vod_type[0] if x_vod_type != [] else ""
            x_vod_player = x_vod.xpath(
                './/div[contains(@class,"qy-search-player-source")]//em[@class="player-name"]/text()')
            vod_dict['vod_player'] = x_vod_player[0] if x_vod_player != [] else ""
            if vod_dict['vod_type'] != "电影" and vod_dict['vod_type'] != "电视剧":
                continue
            if vod_dict['vod_player'] != "爱奇艺":
                continue
            vod_detail = x_vod.xpath(
                './/div[@class="result-figure"]//a[@class="qy-mod-link"]')[0]
            vod_dict['vod_href'] = "https:"+vod_detail.xpath('./@href')[0]
            vod_dict['vod_pic'] = "https:"+vod_detail.xpath('./img/@src')[0]
            vod_dict['vod_name'] = vod_detail.xpath('./@title')[0]
            vod_dict['vod_continu'] = vod_detail.xpath(
                './/span[@class="qy-mod-label"]/text()')[0]
            vod_list.append(vod_dict)
        return vod_list

    def i_album(self, vod_detail_url):  # 获取剧集列表
        html = self.get_web_data.get_html(vod_detail_url)
        album_id = html.xpath(
            '//div[contains(@class,"album-head-info")]//div[contains(@class,"intro-effect")]/@data-score-tvid')[0]
        res_json = self.get_web_data.get_json(
            'https://pcw-api.iqiyi.com/albums/album/avlistinfo?aid=%s&page=1&size=1000' % album_id)
        vod_list = res_json['data']['epsodelist']
        return vod_list

    def i_video(self, vod_url):  # 解析视频地址
        jiexi_url = "https://okjx.cc/jiexi/?url="+vod_url
        # https://www.administrator5.com/admin.php?url=
        # https://www.xn--eqr49pmpixzv.com/index.php?url=
        # http://okxj.cc/?url=
        # https://okjx.cc/jiexi/?url=
        # self.get_web_data.get_html(jiexi_url)
        return jiexi_url

    def i_jeixi(self, vod_url):
        base_url = "https://www.administratorm.com/WANG.WANG/index.php?url="+vod_url
        referer = "https://www.administratorm.com/index.php?url="+vod_url
        html = self.get_web_data.get_html(base_url, referer=referer)
        if html is None:
            return False
        x_script = html.xpath('//script[contains(text(),"var vkey =")]/text()')
        if x_script:
            script_str = x_script[0]
            vkey = re.search(r"(var\svkey\s\=\s\'\S*?\')",
                             script_str).group().split("'")[1]
            print(vkey)
        else:
            print('无数据')
