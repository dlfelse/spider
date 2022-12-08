# coding=utf-8
from lxml import etree
import requests
requests.adapters.DEFAULT_RETRIES = 5
import logging
import linecache
import re
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
proxies = {
    'http': 'http://' + '127.0.0.1:1080',
    'https': 'https://' + '127.0.0.1:1080'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101Firefox/38.0'}


def getUrl():
    baseUrl = 'https://matsuri.5ch.net/test/read.cgi/voiceactor/1555518637/'
    dictAB = {}
    pattern3 = re.compile('https(.*?).jpg', re.S)
    target = requests.get(url=baseUrl, proxies=proxies)
    html = etree.HTML(target.text)
    target.close()
    result = html.xpath('/html/body/div[2]/div/nbsp/dl//dt/a/@href')
    for i in result:
        target1 = requests.get(url=i, proxies=proxies).text
        result2 = re.findall('https(.*?).jpg', target1)
        for j in result2:
            with open('photo.txt', 'a', encoding='utf-8') as file:
                file.write('https' + j + '.jpg' + '\n')


def downPhoto(link):
    try:
        r = requests.get(link[:-1], proxies=proxies, timeout=3)
        fw = open('F:\pic\ch\shuilaiqi' + link[-12:-5] + '.jpg', 'wb')
        fw.write(r.content)
        r.close()
    except:
        logging.debug(link + 'is wrong')




def getSUrl(louurl):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    target1 = requests.get(louurl, proxies=proxies,headers=headers).text
    result2 = etree.HTML(target1)
    hrefs = result2.xpath('/html/body/div[1]/div[6]//div/div[2]/span//a/@href')
    # texts = result2.xpath('/html/body/div[1]/div[6]//div/div[2]/span/text()')
    texts = result2.xpath('/html/body/div[1]/div[6]/div[1]/div[2]/span/text()')
    # for j in hrefs:
    #     # downPhoto('https' + j + '.jpg')
    #     print('https' + j + '.jpg')
    data = result2.xpath('/html/body/div[1]/div[6]/div[1]/div[1]/span[3]/text()')
    line = ""
    for k in texts:
        line = line + " " + k
    try:
        with open('../data/2/shuilaiqi.txt', 'a', encoding='utf-8') as file:
            file.write(dictp.get(dd) + " " + data[0] + "   " + line)
            file.write('\n')
        with open('../data/2/shuilaiqip.txt', 'a', encoding='utf-8') as file:
            for p in hrefs:
                file.write(dictp.get(dd) + " " + data[0] + "   " + p)
                file.write('\n')
    except:
        logging.debug("写入出错")



allpage = linecache.getlines('../data/2/photo2.txt')
dictp ={}
for ap in allpage:
    dictp[ap.split("  ")[1][:-1]] = ap.split("  ")[0]

for dd in dictp.keys():
    print(dd + "   " + dictp.get(dd))
    for nm in range(1,1000):
        print("正在爬取第" + str(nm) + "楼>>>>>>>>>>")
        getSUrl(dd + str(nm))




# for i in range(1,1000):
#     uuu = 'https://matsuri.5ch.net/test/read.cgi/voiceactor/1532675297/' + str(i)
#     print("正在爬取第" + str(i) + "楼>>>>>>>>>>")
#     try:
#         getSUrl(uuu)
#     except:
#         logging.debug(str(i) + "楼不存在")


# str = linecache.getlines('photo2.txt')
# pool.map(downComment,str)  # 多线程工作
# pool.close()
# pool.join()