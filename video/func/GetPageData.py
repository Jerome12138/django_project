import json, re, time
import random
import logging
import traceback
from queue import Queue, LifoQueue
import threading
from . import DBHandler
from . import getRequest

logger = logging.getLogger('log')

def get_vod_data(vod_id):   # 根据vod_id爬取数据，返回数据字典
    # 1.获取数据
    html = getRequest.get_html(
        "http://www.zuidazy4.com/?m=vod-detail-id-%s.html" % vod_id)
    if not html:
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
    html = getRequest.get_html(
        "http://zuidazy4.com/index.php?m=vod-search-pg-%s-wd-%s.html" % (page_index, wd))
    if not html:
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

def run_use_more_thread(func, count=1):   # 运行多线程
    for i in range(count):
        t = threading.Thread(target=func)
        t.setDaemon(True)
        t.start()

class getAllData(object):   # 获取所有数据
    def __init__(self, url, url_index=1):
        self.url_temp = url
        self.url_index = url_index
        self.updated = 0
        self.page_size = 40
        self.url_queue = LifoQueue()    # 先进后出
        self.page_queue = Queue()    # 先进先出
        self.error_pages = []

    def parse_url(self, url):  # 发送请求，获取响应
        return getRequest.get_json(url)

    def get_update_count(self, url_index):   # 获取今日更新数量
        try:
            # 1.匹配来源
            if url_index == 1:
                url = "http://www.zuidazy4.net/"
                x_match = "//li[contains(text(),'今日更新：')]/strong/text()"
            else:
                url = "http://cj.bajiecaiji.com/"
                x_match = "//a[contains(string(),'今日更新：')]/font[2]/text()"
            # 2.获取数据
            html = getRequest.get_html(url)
            if not html:
                update_count = 480
                return update_count
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
            # logger.error('首页请求无数据')
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
            logger.error('page:%s%s'% (url.split('?p=')[1], '请求无数据，放入错误列表'))
            # self.url_queue.put(url)
            self.error_pages.append(url.split('?p=')[1])
        else:
            if int(url.split('?p=')[1]) % 100 == 0:
                print('获取到page:', url.split('?p=')[1])
            self.page_queue.put(res_dict)
        self.url_queue.task_done()

    @run_forever
    def save_data(self):    # 保存数据至数据库
        res_dict = self.page_queue.get()
        # 匹配站点
        if self.url_index == 1:
            is_saved = DBHandler.dump_bulk_data(res_dict['data'])
        elif self.url_index == 2:
            is_saved = DBHandler.dump_bulk_data_url2(res_dict['data'])
        else:
            raise Exception('url参数错误(save_data)')
        if not is_saved:
            logger.error('%s保存出现错误' % res_dict['page']['pageindex'])
            self.page_queue.put(res_dict)
        else:
            self.updated += len(res_dict['data'])
            if int(res_dict['page']['pageindex']) % 100 == 0:
                print('page%s保存成功' % res_dict['page']['pageindex'])
        self.page_queue.task_done()

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
                update_count = 480
                # update_count = self.get_update_count(self.url_index)
            else:
                update_count = up_count if up_count < 10000 else 10000
            update_page = (update_count-1)//self.page_size + 1
        else:   # 更新所有数据
            print('一共%s页数据' % update_page)
            page_thread = 30
            save_thread = 10
        if update_page:
            # 获取下页数据
            self.add_url_to_queue(update_page)
            run_use_more_thread(self.add_page_to_queue, page_thread)
            run_use_more_thread(self.save_data, save_thread)
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
    def i_search(self, wd):  # 搜索视频
        html = getRequest.get_html('https://so.iqiyi.com/so/q_'+wd)
        if not html:
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
        html = getRequest.get_html(vod_detail_url)
        album_id = html.xpath(
            '//div[contains(@class,"album-head-info")]//div[contains(@class,"intro-effect")]/@data-score-tvid')[0]
        res_json = getRequest.get_json(
            'https://pcw-api.iqiyi.com/albums/album/avlistinfo?aid=%s&page=1&size=1000' % album_id)
        vod_list = res_json['data']['epsodelist']
        return vod_list

    def i_video(self, vod_url):  # 解析视频地址
        jiexi_url = "https://okjx.cc/jiexi/?url="+vod_url
        # https://www.administrator5.com/admin.php?url=
        # https://www.xn--eqr49pmpixzv.com/index.php?url=
        # http://okxj.cc/?url=
        # https://okjx.cc/jiexi/?url=
        # getRequest.get_html(jiexi_url)
        return jiexi_url

    def i_jeixi(self, vod_url):
        base_url = "https://www.administratorm.com/WANG.WANG/index.php?url="+vod_url
        referer = "https://www.administratorm.com/index.php?url="+vod_url
        html = getRequest.get_html(base_url, referer=referer)
        if not html:
            return False
        x_script = html.xpath('//script[contains(text(),"var vkey =")]/text()')
        if x_script:
            script_str = x_script[0]
            vkey = re.search(r"(var\svkey\s\=\s\'\S*?\')",
                             script_str).group().split("'")[1]
            print(vkey)
        else:
            print('无数据')


def getDoubanInfo(wd):  # 爬虫
    url = "https://search.douban.com/movie/subject_search?search_text=%s&cat=1002" % wd
    html = getRequest.get_html(url,is_proxy=1)
    if not html:
        return False
    data_list = html.xpath('//div[@class="root"]//text()')
    print(data_list)
    return data_list


def getRating(douban_id):   # 根据豆瓣id获取评分
    try:
        url = "https://api.douban.com/v2/movie/subject/%s?apikey=0df993c66c0c636e29ecbb5344252a4a" % douban_id
        vod_info = getRequest.get_json(url,is_proxy=1)
        if vod_info:
            # print(vod_info['rating']['average'])
            return vod_info['rating']['average']
        else:
            return False
    except Exception as e:
        print('get_80s Exception: ',e)
        print(traceback.print_exc())
        return False


def findID(name, vod_year):  # name即剧名
    try:
        url = 'https://movie.douban.com/j/subject_suggest?q=%s' % name
        item_list = getRequest.get_json(url,is_proxy=1)
        if not item_list:
            return None
        # 从item_list中的每个item中提取对应的ID值
        id_list = []  # ID存放列表
        for item in item_list:
            # print(item)
            if item.get('year') == vod_year:   # 1.同年
                id_list.append(item)
        if len(id_list) == 1:   # 只有一条数据
            return id_list[0]['id']
        elif len(id_list) == 0:   # 无数据
            # if name != '爱情公寓2':
            #     print(name, '未匹配到合适id')
            return None
        else:   # 匹配到了多个ID（可能是同名不同剧）
            return [item['id'] for item in id_list]
    except Exception as e:  # 如果不能正常运行上述代码（不能访问网页等），输出未成功的剧名name。
        print('findID ERROR:', name, e)
        return None


class Get80sScore(object):
    def __init__(self):
        self.url_temp = 'https://www.80s.tw/movie/list/-%s----p/%s'
        # https://www.80s.tw/ju/list/---2019-0--p/2
        # 'https://www.80s.tw/movie/list/-%s----p/%s'
        self.data_queue = Queue()    # 先进先出
        self.error_list = []
        self.detail_list = []
        self.timeout = 0
        self.count = 0
    
    def get_page(self): # 获取80s页面
        try:
            page_list = []
            for year in range(2020, 2007, -1):
                html = getRequest.get_html(self.url_temp % (year, 1))
                last_pager = html.xpath('//div[@class="pager"]/a[contains(text(),"尾页")]/@href')
                if last_pager != []:
                    page_count = int(last_pager[0].split('/')[-1])
                else:
                    print('获取页数错误：',last_pager)
                    page_count = 1
                print('%s共%s页数据'%(year,page_count))
                for page_index in range(1,page_count+1):
                    page_list.append((str(year),page_index))
                with open('80s_list.json','w',encoding='utf-8') as f:
                    json.dump(page_list,f)
                    print('页面列表保存成功')
            return page_list
        except Exception as e:
            print('get_80s Exception: ',e)
            return False

    def get_video(self,year,page_index):    # 获取当前页面的80s视频列表
        video_list = []
        try:
            # if page_index == 1 : # 第一页时输出
            print('开始获取',year,page_index)
            html = getRequest.get_html(self.url_temp % (year,page_index))
            if len(html) == 0:
                self.error_list.append((year,page_index))
                raise Exception('html%s无数据返回' % self.url_temp % (year,page_index))
            li_list = html.xpath('//ul[@class="me1 clearfix"]/li')
            for item_li in li_list: # 爬取视频列表数据
                name = item_li.xpath('./h3/a/text()')[0].strip()
                score = item_li.xpath('./a/span[@class="poster_score"]/text()')
                if score != []: # 有评分，添加进列表
                    vod_data = {
                        'vod_name': name,
                        '80s_url': item_li.xpath('./h3/a/@href')[0],
                        'year':year,
                        'score': score[0].strip(),
                    }
                    video_list.append(vod_data)
            return video_list
        except Exception as e:
            print('get_video_list Exception',url,e)
            return False
        

    def save_score(self,video_data):   # 匹配视频信息并储存评分数据
        try:
            # video_data = dict(video_data)
            vod_info_list = DBHandler.search_data2(video_data['vod_name'].replace(' ',''),video_data['year'])
            if len(vod_info_list) == 0: # 如果无结果
                re_str = re.search(r'(\[第[一二三四五六七八九十]季\])',video_data['vod_name'])
                if re_str is not None:
                    sub_str = re_str.group().lstrip('[').rstrip(']')
                    video_data['vod_name'] = re.sub(r'\[%s\]'%sub_str,sub_str,video_data['vod_name'])
                    return self.save_score(video_data)
                re_str2 = re.search(r'(\/)',video_data['vod_name'])
                if re_str2 is not None:
                    video_data['vod_name'] = video_data['vod_name'].split('/')[0]
                    return self.save_score(video_data)
                re_str3 = re.search(r'(第[一二三四五六七八九十]季)',video_data['vod_name'])
                if re_str3 is not None:
                    video_data['vod_name'] = re.sub(re_str3.group(),'',video_data['vod_name'])
                    return self.save_score(video_data)
                re_str4 = re.search(video_data['year'],video_data['vod_name'])
                if re_str4 is None:
                    video_data2 = dict(video_data)
                    video_data2['vod_name'] = video_data['vod_name']+video_data['year']
                    return self.save_score(video_data2)
            if len(vod_info_list) == 2:   # 如果匹配到多项
                # video_data1 = list(video_data)
                video_data2 = dict(video_data)
                # video_data1['vod_name'] = video_data1['vod_name']+'国语'
                # flag1 = self.save_score(video_data1)
                video_data2['vod_name'] = video_data2['vod_name']+'粤语'
                flag2 = self.save_score(video_data2)
                if flag2:
                    return True
                else:
                    return False
            elif len(vod_info_list) == 1:   # 如果只有一项
                if vod_info_list[0].vod_douban_id: # 如果已存在豆瓣id,则返回
                    # self.detail_list.remove(video_data)
                    return True
                else:
                    res = self.get_detail(video_data['80s_url'])    # 获取详情
                    if res: # 正常返回结果
                        if res == -1:   # 搜索无数据
                            return
                        (douban_id,rating) = res
                        print(vod_info_list[0].vod_name, douban_id, rating,end='')
                        DBHandler.dump_douban_id(vod_info_list[0].vod_id, douban_id)
                        DBHandler.dump_rating(vod_info_list[0].vod_id, rating)
                        print(' 保存成功[80s]')
                        self.timeout = 0
                        # time.sleep(1 + float(random.randint(0, 100)) / 100)
                        return True
                    else:   # 异常
                        self.timeout += 1
                        time.sleep(180)
                        if self.timeout == 5:
                            print('----80s连续五次失败，等待30分钟---')
                            time.sleep(1800)
                        elif self.timeout > 10:
                            print('-----80s连续十次失败，等待2h-----')
                            time.sleep(7200)
                        print('----------80s重新启动查找------------')
        except Exception as e:
            print('save_score Exception:',video_data['vod_name'],e)
            print(traceback.print_exc())
            return False


    def get_detail(self,url):    # 获取豆瓣id
        try:
            html = getRequest.get_html('https://www.80s.tw%s'%url)
            if not html:
                print('https://www.80s.tw%s'%url,'无数据返回')
                self.error_list.append(page)
                return False
            x_rating = html.xpath('//div[@class="info"]/div[@class="clearfix"]//span[contains(text(),"豆瓣评分：")]/../text()')
            x_douban_id = html.xpath('//div[@class="info"]/div[@class="clearfix"]//a[contains(text(),"豆瓣短评")]/@href')
            if len(x_rating)>=1 and len(x_douban_id)==1:
                vod_score = x_rating[2].strip()
                vod_douban_id = x_douban_id[0].split('/')[-2]
                return (vod_douban_id,vod_score)
            elif len(x_douban_id)==0:
                print('无豆瓣id数据:',x_rating,x_douban_id,url)
                return -1
            else:
                print('detail:',x_rating,x_douban_id,url)
                return False
        except Exception as e:
            print('get_detail Exception',url,e)
            return False
        

    def run(self):  # 主程序逻辑
        page_list = []
        return_flag = False
        try:
            # 2.获取80s页面中有豆瓣评分的电影数据
            with open('80s_detail_list.json','r',encoding='utf-8') as f:
                self.detail_list = json.load(f)
            print('共有80s视频：%s' % len(self.detail_list))
            if len(self.detail_list) == 0: # 无视频列表则重新获取
                print('视频列表为空，重新获取')
                # 1.获取80s页面
                with open('80s_list.json','r',encoding='utf-8') as f:
                    page_list = json.load(f)
                if len(page_list) != 0: # 已存在目录
                    print('共有80s页面：%s' % len(page_list))
                else:
                    page_list = self.get_page()
                for page in page_list:
                    video_list = self.get_video(*page)
                    self.detail_list.extend(video_list)
                    # time.sleep(5) # 每3分钟获取一次页面
                if len(self.detail_list)!=0:
                    with open('80s_detail_list.json','w',encoding='utf-8') as f:
                        json.dump(self.detail_list,f,ensure_ascii=False, indent=4)
                        print('详情页列表保存成功')
            # 3.将电影数据与数据库数据对比，匹配则储存评分
            for video_data in self.detail_list:
                self.count+=1
                if self.save_score(video_data):
                    self.detail_list.remove(video_data)
                if self.count%50==0:
                    print('已读取80s数据:%s'%self.count)
                    with open('80s_detail_list.json','w',encoding='utf-8') as f:
                        json.dump(self.detail_list,f,ensure_ascii=False, indent=4)
                        print('详情页列表已更新')
            print('------80s获取完毕-----')
            print('错误列表：',self.error_list)
            return_flag = True
        except Exception as e:
            print('80s_main Exception:')
            print(traceback.print_exc())
        finally:
            if len(self.detail_list)!=0:
                with open('80s_detail_list.json','w',encoding='utf-8') as f:
                    json.dump(self.detail_list,f,ensure_ascii=False, indent=4)
                    print('详情页列表保存成功')
            return return_flag

def get_douban_data():
    try:
        type_list = ['movie','tv']
        tag_list = {
            'movie': ['热门','最新','经典','可播放','豆瓣高分','冷门佳片','华语','欧美','韩国','日本','动作','喜剧','爱情','科幻','悬疑','恐怖','治愈'],
            'tv': ['热门','美剧','英剧','日剧','国产剧','港剧','日本动画','综艺','纪录片']
        }
        for video_type in type_list:
            for tag in tag_list[video_type]:
                with open('douban_list.json','r',encoding='utf-8') as f:
                    detail_list = json.load(f)
                # if detail_list[video_type][tag]:
                #     pass
                print('%s %s 开始获取'%(video_type, tag))
                url = 'https://movie.douban.com/j/search_subjects?type=%s&tag=%s&sort=%s&page_limit=%s&page_start=%s' % (video_type, tag, 'time', 1000, 0)
                item_list = getRequest.get_json(url,is_proxy=1)
                print('%s %s 获取成功'%(video_type, tag))
                # print(item_list)
                if not item_list or not item_list['subjects']:
                    print('item_list:', item_list)
                    return None
                # print(item_list['subjects'])
                print('%s %s 数据总数：%s'%(video_type, tag, len(item_list['subjects'])))
                detail_list[video_type].extend(item_list['subjects'])

                if len(detail_list)!=0:
                    with open('douban_list.json','w',encoding='utf-8') as f:
                        json.dump(detail_list,f,ensure_ascii=False, indent=4)
                        print('%s %s 保存成功'%(video_type, tag))
                time.sleep(10)
    except Exception as e:
        print('get_douban_data ERROR:', e)
        return None


def match_score_by_name(video_data):   # 匹配视频信息并储存评分数据
    try:
        # video_data = dict(video_data)
        vod_info_list = DBHandler.search_data(video_data['title'].replace(' ',''))
        # print(vod_info_list)
        if len(vod_info_list) == 0: # 如果无结果
            re_str = re.search(r'(\[第[一二三四五六七八九十]季\])',video_data['title'])
            if re_str is not None:
                sub_str = re_str.group().lstrip('[').rstrip(']')
                video_data['title'] = re.sub(r'\[%s\]'%sub_str,sub_str,video_data['title'])
                return match_score_by_name(video_data)
            re_str2 = re.search(r'(\/)',video_data['title'])
            if re_str2 is not None:
                video_data['title'] = video_data['title'].split('/')[0]
                return match_score_by_name(video_data)
            re_str3 = re.search(r'(第[一二三四五六七八九十]季)',video_data['title'])
            if re_str3 is not None:
                video_data['title'] = re.sub(re_str3.group(),'',video_data['title'])
                return match_score_by_name(video_data)
        if len(vod_info_list) == 2:   # 如果匹配到多项
            # video_data1 = list(video_data)
            video_data2 = dict(video_data)
            # video_data1['title'] = video_data1['title']+'国语'
            # flag1 = match_score_by_name(video_data1)
            video_data2['title'] = video_data2['title']+'粤语'
            flag2 = match_score_by_name(video_data2)
            if flag2:
                return True
            else:
                return False
        elif len(vod_info_list) == 1:   # 如果只有一项
            # print(vod_info_list[0]['vod_douban_id'])
            if vod_info_list[0]['vod_douban_id']: # 如果已存在豆瓣id,则返回
                return True
            else:
                print(vod_info_list[0]['vod_name'], video_data['id'], video_data['rate'],end='')
                DBHandler.dump_douban_id(vod_info_list[0]['vod_id'], video_data['id'])
                DBHandler.dump_rating(vod_info_list[0]['vod_id'], video_data['rate'])
                print(' 保存成功[douban]')
                return True
    except Exception as e:
        print('match_score_by_name Exception:',video_data['title'],e)
        # print(traceback.print_exc())
        return False


def match_score_from_jsondata(video_data):   # 匹配视频信息并储存评分数据
    try:
        # video_data = dict(video_data)
        vod_info_list = DBHandler.search_data2(video_data['title'].replace(' ',''),video_data['year'])
        # print(vod_info_list)
        if len(vod_info_list) == 0: # 如果无结果
            re_str = re.search(r'(\[第[一二三四五六七八九十]季\])',video_data['title'])
            if re_str is not None:
                sub_str = re_str.group().lstrip('[').rstrip(']')
                video_data['title'] = re.sub(r'\[%s\]'%sub_str,sub_str,video_data['title'])
                return match_score_by_name(video_data)
            re_str2 = re.search(r'(\/)',video_data['title'])
            if re_str2 is not None:
                video_data['title'] = video_data['title'].split('/')[0]
                return match_score_by_name(video_data)
            re_str3 = re.search(r'(第[一二三四五六七八九十]季)',video_data['title'])
            if re_str3 is not None:
                video_data['title'] = re.sub(re_str3.group(),'',video_data['title'])
                return match_score_by_name(video_data)
        if len(vod_info_list) == 2:   # 如果匹配到多项
            # video_data1 = list(video_data)
            video_data2 = dict(video_data)
            # video_data1['title'] = video_data1['title']+'国语'
            # flag1 = match_score_by_name(video_data1)
            video_data2['title'] = video_data2['title']+'粤语'
            flag2 = match_score_by_name(video_data2)
            if flag2:
                return True
            else:
                return False
        elif len(vod_info_list) == 1:   # 如果只有一项
            # print(vod_info_list[0]['vod_douban_id'])
            if vod_info_list[0].vod_douban_id: # 如果已存在豆瓣id,则返回
                return True
            else:
                print(vod_info_list[0].vod_name, video_data['id'], video_data['rate'],end='')
                DBHandler.dump_douban_id(vod_info_list[0].vod_id, video_data['id'])
                DBHandler.dump_rating(vod_info_list[0].vod_id, video_data['rate'])
                print(' 保存成功[douban_json]')
                return True
    except Exception as e:
        print('match_score_from_jsondata Exception:',video_data['title'],e)
        # print(traceback.print_exc())
        return False