# coding=utf-8
import requests
requests.adapters.DEFAULT_RETRIES = 5
from base import tool
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)

alllink = tool.getAllPages('https://qingbuyaohaixiu.com/?page=',1,5)

def newSpider(url):
    try:
       pothourl = tool.getTarget(url,'/html/body/div[2]/div[1]/div[1]/amp-img/@src')
       name = tool.getTarget(url,'/html/body/div[2]/div[1]/div[1]/h3/text()')
       if len(name) > 0:
           tool.downPhoto(pothourl[0],'F:\shy\ ',name[0])
       else:
           print(url + "    is null")
    except:
       print(name[0] + 'download is wrong')



tot_page = []

#按照页面获得图片链接
for link in alllink:
    pageurl = tool.getTarget(link,'/html/body/div[2]//div//div/a[1]/@href')
    for u in pageurl:
        tot_page.append('https://qingbuyaohaixiu.com' + u)


#循环获得图片链接
for i in range(18500,18516):
    tot_page.append('https://qingbuyaohaixiu.com/post/' + str(i))

pool = ThreadPool(4)  # 双核电脑
pool.map(newSpider, tot_page)  # 多线程工作
pool.close()
pool.join()
