# coding=utf-8
from lxml import etree
import requests
requests.adapters.DEFAULT_RETRIES = 5
import logging
from base import tool
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
headers = {'Connection': 'close',
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}

filepath = 'F:\pic\lyn\ '
rooturl = 'https://peachring.com/weibo/user/1765893783/'


target = requests.get(rooturl,headers=headers, timeout=10)
html = etree.HTML(target.text)
target.close()
#获得下一页URL
nexturl = html.xpath('/html/body/div[1]/div[3]/div/div[2]/div[2]/a[2]/@href')\
#全体url列表
allurl = []


#获得所有页面网址
for i in range(0,100):
    try:
        newurl = rooturl + nexturl[0]
        print(newurl)
        target = requests.get(newurl, headers=headers, timeout=10)
        html = etree.HTML(target.text)
        target.close()
        nexturl = html.xpath('/html/body/div[1]/div[3]/div/div[2]/div[2]/a[2]/@href')
        tool.writetotxt('a.txt',rooturl + nexturl[0])
    except:
        print(newurl + '!!!!!!!!!!!!')




tots = tool.getStrFromText('a.txt')

for url in tots:
    try:
        target = requests.get(url, headers=headers, timeout=10)
        html2 = etree.HTML(target.text)
        target.close()
        links = html2.xpath('/html/body/div[1]/div[3]/div/div[2]/div[1]//*/div[2]/ul//*/img/@layer-src')
        for link in links:
            tool.writetotxt('b.txt', link)
        print(links[0]+ '~~~~~~~~~')
    except:
        print(url + 'wrong!!!!!!!!')

def downPhotos(sss):
    filename = sss.split("/")[-1];
    link = sss;
    try:
        r = requests.get(link, headers=headers, timeout=15)
        fw = open(filepath + filename, 'wb')
        fw.write(r.content)
        r.close()
    except:
        logging.debug(link + 'is wrong')



pool = ThreadPool(50) #双核电脑
tot_page = tool.getStrFromText('b.txt')
pool.map(downPhotos, tot_page)#多线程工作
pool.close()
pool.join()