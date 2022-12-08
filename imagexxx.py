# coding=utf-8
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests

from base import tool
requests.adapters.DEFAULT_RETRIES = 5
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)




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






def writetotxt(filename,str):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(str)
        file.write('\n')


seiyuu='kousaka-sumire'
allpage = 21


alllink = tool.getAllPages('https://zh.porn-image-xxx.com/search/tag/' + seiyuu + '/page/',1,allpage)
#按照页面获得图片链接
strline = []
for link in alllink:
    pageurl = tool.getTarget(link,'//*[@id="image-list"]//li/div/p[1]/a/@href')
    for u in pageurl:
        strline.append('https://zh.porn-image-xxx.com/' + u)

allline = []
for line in strline:
    for pm in range(1,500):
        singlepageurl = tool.getTarget(line + 'page/' + str(pm),'//*[@id="display_image_detail"]//div/a[1]/img/@src')
        if len(singlepageurl)>0:
            for sx in range(0,len(singlepageurl)):
                allline.append(singlepageurl[sx])
        else:
            break

def imageSpider(i):
    try:
        tool.downPhoto(i,'F:\imagexxx\jin\ ',i.split('/')[4] + '_' + i.split('/')[8][:-4])
    except:
        writetotxt('../test/pornb.txt', i)

pool = ThreadPool(4)  # 双核电脑
pool.map(imageSpider, allline)  # 多线程工作
pool.close()
pool.join()

# allurl = []








        # tot_page.append('https://qingbuyaohaixiu.com' + u)


#循环获得图片链接
# for i in range(1,10100):
#     tot_page.append('https://qingbuyaohaixiu.com/post/' + str(i))

# pool = ThreadPool(4)  # 双核电脑
# pool.map(newSpider, tot_page)  # 多线程工作
# pool.close()
# pool.join()









#nico爬虫
# pageurl = crawler.tool.getTarget('https://www.nicovideo.jp/watch/sm36342881','/html/body/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div/div//div/@title')
#
# for com in pageurl:
#     print(com)

