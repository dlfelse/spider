import re

from lxml import etree
import requests
from base import tool
requests.adapters.DEFAULT_RETRIES = 5
import importlib,sys

importlib.reload(sys)

#进入豆瓣中某位演员的图片所在页面，选择按时间排序，经分析此时的链接，到下一页的时候，只有start的值增加了30，所以主要对start
url1 = 'https://movie.douban.com/celebrity/1054453/photos/?type=C&start='
url2 = '&sortby=like&size=a&subtype=a'
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
num =1
for i in range(0,76):
    i = 30*i
    url = url1 + str(i) + url2
    try:
        target1 = requests.get(url, headers=headers)
        html = etree.HTML(target1.text)
        target1.close()
        resurls = html.xpath('/html/body/div[3]/div[1]/div/div[1]/ul//li/div[1]/a/@href')
        for i in resurls:
            num = num + 1
            ml = tool.getTarget(i,'/html/body/div[3]/div[1]/div/div[1]/div[2]/div/a[1]/img/@src')
            print(ml[0])
            tool.writetotxt('../data/ddd.txt','douban_scart'+str(num) + ' ' + ml[0])
    except:
        print (i/30)