# coding=utf-8
from lxml import etree
import requests
requests.adapters.DEFAULT_RETRIES = 5
import linecache
import re
import importlib,sys
importlib.reload(sys)



#
# def geturls(target):
#     html = etree.HTML(target.text)
#     resurl = html.xpath('//*[@id="masonry_container"]//div/a/img/@data-src | //*[@id="masonry_container"]/div/a/@href')
#     for i in range(0,len(resurl)):
#         if i % 2 ==0:
#             baseUrl = resurl[i+1].replace('/300/','/620/')
#             ttt = requests.get('https://www.sex.com' + resurl[i])
#             html2 = etree.HTML(ttt.text)
#             title = html2.xpath('/html/head/title')
#             newUrl = baseUrl

def spider(url):
    print(url)
    print('当前执行URL:' + url)
    html = requests.get(url)
    geturls(html)
    print('当前执行URL:' + url + '已完成')

# urls = []
# au = linecache.getlines('sexall.txt')
# for a in au:
#     if a not in dictD:
#         urls.append(a[0:-1])
#
# @retry(tries=5,delay=2)
# def downPhoto(i,testurl,headers):
#     target = requests.get(testurl,headers=headers,timeout=3)#,proxies=get_random_ip())
#     html = etree.HTML(target.text)
#     turl = html.xpath('//*[@class="image_frame"]//img/@src')
#     print(turl)
#     r = requests.get(turl[0], headers=headers, timeout=3)#,proxies=get_random_ip())
#     return r
#
#
#
# def spider2(i):
#     testurl = 'https://www.sex.com' + i
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36',
#     'Referer':'https://www.sex.com' + i}  ##浏览器请求头（大部分网站没有这个请求头会报错、请务必加上哦）
#     try:
#         r = downPhoto(i,testurl,headers)
#         fw = open('F:\sex\ ' + i.split("/")[-2] + '.gif', 'wb')
#         fw.write(r.content)
#         r.close()
#     except:
#         print(testurl)
#
#
#
# pool = ThreadPool(10)  # 双核电脑
# pool.map(spider2, urls)  # 多线程工作
# pool.close()
# pool.join()


#图片下载无法根据链接获得
def geturls(target):
    html = etree.HTML(target.text)
    resurl = html.xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/img/@src')
    r = requests.get('https://cdn.sex.com/images/pinporn/2020/01/16/22503423.jpg?width=620&site=sex&user=adryadry')
    fw = open('F:\sex\gif\ test.jpg ', 'wb')
    print('downloading:' + 'test.jpg')
    fw.write(r.content)
    # for url in resurl:
    #     r = requests.get('https://cdn.sex.com/images/pinporn/2020/01/16/22503423.jpg?width=620&site=sex&user=adryadry')
    #     if url.endswith('gif'):
    #         path = 'F:\sex\gif\ ' + url[46:55] + '.gif'
    #     else:
    #         path = 'F:\sex\pic\ ' + url[46:55] + '.jpg'
    #     if os.path.exists(path):
    #         continue
    #     fw = open(path, 'wb')
    #     print('downloading:' + path)
    #     fw.write(r.content)
    print('down')


def getListFromPath(pathroute):
    strLine = []
    ipstr = linecache.getlines(pathroute)
    for ip in ipstr:
        strLine.append(ip[0:-1])
    return strLine


#获取视频下载链接存入xunlei
def getVideoLink(tt):
    newhtml = requests.post('https://www.sex.com/video/stream/' + tt[0], allow_redirects=False, timeout=5)
    print(newhtml.headers['location'])
    with open('xunlei.txt', 'a', encoding='utf-8') as file:
        file.write(newhtml.headers['location'] + '\n')

#获得某页面内所有单个PIN的链接
def getSinglePinFromPage(link):
    target = requests.get(link,timeout=10)  # , proxies=proxies)
    html = etree.HTML(target.text)
    resurl = html.xpath('//*[@id="masonry_container"]//div/a[@class="image_wrapper"]/@href')
    trel = html.xpath('//*[@id="masonry_container"]//div/div[1]/a//text()')
    for tn in range(0, len(resurl)):
        # repines      likes          comments
        if int(trel[tn * 3]) > 300 and int(trel[tn * 3 + 1]) > 300 and int(trel[tn * 3 + 2]) > 4:
            with open('sexall.txt', 'a', encoding='utf-8') as file:
                file.write(resurl[tn] + '\n')

#初始URL及循环页数
#'https://www.sex.com/videos/?sort=popular&sub=all&page='
#https://www.sex.com/user/dplayer/likes/?page='
#'https://www.sex.com/?sort=popular&sub=all&page='
#'https://www.sex.com/pics/?sort=popular&sub=all&page='
# for i in range(1,3):
#     pageUrl = 'https://www.sex.com/pics/?sort=popular&sub=all&page=' + str(i)
#     try:
#         getSinglePinFromPage(pageUrl)
#     except:
#         print(pageUrl + 'error')

#从sexall中读取单个pin的url
allUrl = getListFromPath('sexall.txt')
for url in allUrl:
    target = requests.get('https://www.sex.com' + url, timeout=5)
    tt = re.findall('\'\/video\/stream\/(.*?)\',', target.text)
    #判断是否为视频或图片
    if len(tt)>0:
        getVideoLink(tt)
    else:
        geturls(target)












