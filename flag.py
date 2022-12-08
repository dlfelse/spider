# coding=utf-8
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
requests.adapters.DEFAULT_RETRIES = 5
import os.path
import re
from bs4 import BeautifulSoup
import urllib
import os
import linecache
import sys
import time
import crawler.tool
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:73.0) Gecko/20100101 Firefox/73.0',
    'Host': 'flapi.nicovideo.jp',
    'Cookie': 'nicosid=1582208436.2035246214; _ga=GA1.1.526826609.1582208439; nico_gc=srch_s%3Dm%26srch_o%3Dd; _ga_8W314HNSE8=GS1.1.1582212763.2.1.1582214070.0; nicohistory=sm26139188%3A1582213110%3A1582213110%3Adc431123f4a92b01%3A7%2Csm26123818%3A1582209361%3A1582209361%3Ac37e9021d9149ee7%3A3; user_session=user_session_66863438_8496265df1534947ebe40217f577f691497739a1aeb9c5b82be8fb4b08ac3961'

}


def getCommentFromSm(sm):
    url1 = 'http://flapi.nicovideo.jp/api/getflv' + sm
    target = requests.get(url1, headers=headers, proxies=crawler.tool.getProxies(), timeout=6)
    # 匹配得到相关数值
    thread_id = re.findall(r'thread_id=(\d+)&', target.text)[0]
    user_id = '66863438'
    time_ms = re.findall(r'time=(\d+)&', target.text)[0]
    userkey = re.findall(r'&userkey=(.*)', target.text)[0]
    # 获得way
    url2 = ('http://flapi.nicovideo.jp/api/getwaybackkey?thread=' + str(thread_id) + '&when=' + str(time_ms))
    target2 = requests.get(url2, headers=headers, proxies=crawler.tool.getProxies(), timeout=6)
    waybackkey = re.findall(r'waybackkey=(.*)', target2.text)[0]
    url3 = 'https://nmsg.nicovideo.jp/api/thread?version=20090904&res_from=1&user_id=' + user_id + '&language=0&' + 'thread=' + str(
        thread_id) + '&when=' + str(time_ms) + '&waybackkey=' + str(waybackkey)
    req = requests.get(url3, headers=headers, proxies=crawler.tool.getProxies(), timeout=6)
    html = req.content
    html_doc = str(html, 'utf-8')  # 修改成utf-8
    # 解析
    soup = BeautifulSoup(html_doc, "lxml")
    results = soup.find_all('chat')
    contents = [x.text for x in results]
    for oc in contents:
        crawler.tool.writetotxt('flag.txt', oc)
#getCommentFromSm(sm)
#获得所有的sm号
# for i in range(1,7):
#     url = 'https://www.nicovideo.jp/tag/水瀬いのりMELODY_FLAG?page=' + str(i) + '&sort=f&order=d'
#     one = requests.get(url,headers=crawler.tool.headers, proxies=crawler.tool.getProxies(), timeout=6)
#     html =  etree.HTML(one.text)
#     sm = html.xpath('/html/body/div[1]/div[3]/div/div[1]/div[3]/ul[2]//li/div[2]/p/a/@href')
#     for s in sm:
#         crawler.tool.writetotxt('flagsm.txt',s[6:])
allsm = linecache.getlines('../data/2/falgack.txt')
for sm in allsm:
    crawler.tool.writetotxt('flag.txt',sm[:-1])
    try:
        getCommentFromSm(sm[:-1])
    except:
        crawler.tool.writetotxt('falgback.txt',sm[:-1])