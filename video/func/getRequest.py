import json
import random
import requests
from lxml import etree
from . import getProxies
import traceback


user_agents = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

HEADERS = {"User-Agent": random.choice(user_agents)}
proxy_str = "150.138.253.71:808 60.191.11.249:3128 1.119.166.180:8080 58.220.95.78:9401 111.222.141.127:8118 47.106.59.75:3128 58.220.95.80:9401 58.220.95.54:9400 61.240.222.27:3128 1.196.161.10:9999 58.220.95.86:9401 58.220.95.79:10000 58.240.232.122:808 58.220.95.80:9401 58.220.95.79:10000 150.138.253.71:808 58.220.95.78:9401 58.220.95.54:9400 58.220.95.86:9401 1.119.166.180:8080 119.178.101.18:8888"
proxy2 = proxy_str.split(' ')


def get_html(url, is_debug=0, is_proxy=0, *args, **kwargs):
    i = 0
    while i < 3:
        try:
            if kwargs.get('referer'):
                HEADERS['Referer'] = kwargs['referer']
            if is_proxy:
                proxy1 = requests.get(
                    "http://49.234.78.157:5010/get/").json().get('proxy')
                proxy = random.choice(proxy2)
                proxies = {"http": "http://%s" % proxy,
                           "https": "http://%s" % proxy}
            else:
                proxies = {}
            # print(proxy) , proxies=
            res = requests.get(url, headers=HEADERS,
                               proxies=proxies, timeout=(5, 15))
            if res.status_code == 200:
                html_str = res.content.decode()
            else:
                print('爬虫网站%s返回状态码错误：%s' %
                      (url, res.status_code), 'proxy:', proxy)
                return False
            if is_debug:
                with open('htmlres.html', 'w', encoding="utf-8") as f:
                    f.write(html_str)
            html = etree.HTML(html_str)
            if html is None:
                print('html页面返回为空')
                return False
            return html
        except requests.exceptions.ConnectTimeout:
            i += 1
            # print('爬虫网站%s请求超时，重试%s次' % (url, i))
        except requests.exceptions.RequestException:
            print('爬虫网站%s请求错误' % (url), e)
            return False
        except Exception as e: 
            print('get_html ERROR:', e)
            return False
    return False


def get_json(url, is_debug=0, is_proxy=0, *args, **kwargs):
    i = 0
    while i < 3:
        try:
            if kwargs.get('referer'):
                HEADERS['Referer'] = kwargs['referer']
            if is_proxy:
                proxy1 = requests.get(
                    "http://49.234.78.157:5010/get/").json().get('proxy')
                proxy = random.choice(proxy2)
                proxies = {"http": "http://%s" % proxy,
                           "https": "http://%s" % proxy}
            else:
                proxies = {}
            # print(proxy)
            response = requests.get(
                url, headers=HEADERS, proxies=proxies, timeout=(5, 15))
            if response.status_code != 200:
                print('proxy:', proxy, 'Status Code：',
                      response.status_code, '重试')
                i += 1
                proxy2.remove(proxy)
                continue
            res_json = json.loads(response.content.decode())
            return res_json
        except requests.exceptions.ConnectTimeout:
            i += 1
            # print('爬虫网站%s请求超时，重试%s次' % (url, i))
        except requests.exceptions.RequestException as e:
            # print('page%s请求超时，重试%s次' % (url.split('?p=')[1], i))
            print('爬虫网站%s请求错误' % (url))
            # print(traceback.print_exc())
            return False
        except json.decoder.JSONDecodeError:
            i += 1
            print('page jSON解析错误，重试%s次' % i)
            # print('page%s jSON解析错误，重试%s次' % (url.split('?p=')[1], i))
        except Exception as e: 
            print('get_html ERROR:', e)
            return False
    return False
