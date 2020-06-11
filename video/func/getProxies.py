import time
from . import getRequest
from . import DBHandler

import requests

def get_proxy():
    res = requests.get("http://www.xiladaili.com/api/?uuid=7a00f05db31f42cb9eed55da31cffbbf&num=500&place=中国&category=1&protocol=0&sortby=0&repeat=1&format=3&position=1")
    if res.status_code == 200:
        proxy_str = res.content.decode()
        if proxy_str != '调用频率过快':
            print('获取到新的代理：',proxy_str)
            return proxy_str.split(' ')
        else:
            print('调用频率过快')
    time.sleep(600)
    return []

def delete_proxy(proxy):
    requests.get("http://49.234.78.157:5010/delete/?proxy={}".format(proxy))

def IPList_61():
    try:
        proxies = []
        for page in ['1', '2']:    #页码
            url = 'http://www.66ip.cn/%s.html' % page
            html = getRequest.get_html(url)
            if html != None:
                # print(html)
                iplist = html.xpath('//tr')
                i = 0
                for ip in iplist:
                    if i >= 1:  # 从第2个开始获取
                        # print(ip)
                        ip_port = ip.xpath('//td')[0]+':'+ip.xpath('//td')[1]
                        proxies.append(ip_port)
                    i += 1
            time.sleep(1)
        DBHandler.redis_dumplist('ip_port',proxies)
        return True
    except Exception as e:
        print('IPList_61 exception:', e)
        return False
