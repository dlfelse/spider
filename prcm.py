# coding=utf-8
import crawler
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests
requests.adapters.DEFAULT_RETRIES = 5
import os.path
import re
import os
import sys
import time
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)

alllink = crawler.tool.getAllPages('https://prcm.jp/list/松岡禎丞?page=',1,128)
def newSpider(url):
    try:
       pothourl = crawler.tool.getTarget(url,'/html/body/div[1]/img/@src')
       name = url.split("/")[-1];
       if len(name) > 0:
           crawler.tool.downPhoto(pothourl[0],'E:\神祈\松\ ',name)
       else:
           print(url + "    is null")
    except:
       print(name + 'download is wrong')



tot_page = []

#按照页面获得图片链接
for link in alllink:
    pageurl = crawler.tool.getTarget(link,'//*[@id="imglist_container"]/ul//li/a/@href')
    for u in pageurl:
        surl = crawler.tool.getTarget(u,'//*[@id="picture"]/a/@href')
        print(u)
        if len(surl)>0:
           tot_page.append('https://prcm.jp' + surl[0])


#循环获得图片链接
# for i in range(1,10100):
#     tot_page.append('https://qingbuyaohaixiu.com/post/' + str(i))

pool = ThreadPool(4)  # 双核电脑
pool.map(newSpider, tot_page)  # 多线程工作
pool.close()
pool.join()

