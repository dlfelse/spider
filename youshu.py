# coding=utf-8
from lxml import etree
from multiprocessing.dummy import Pool as ThreadPool
import requests

from base import tool

requests.adapters.DEFAULT_RETRIES = 5
import os.path
import re
import os
import sys
import time
import importlib,sys
importlib.reload(sys)
headers = tool.getHeaders()
for i in range(461,500):
    link = 'http://www.yousuu.com/bookstore/?channel&classId&tag&countWord&status&update&sort=scorer&page=' + str(i)
    target = requests.get(link, headers=headers,timeout=10)
    html = etree.HTML(target.text)
    target.close()
    resurl = html.xpath('//*/div[@class="book-info"]/a/text() | //*/div[@class="book-info"]/p[2]/text()')
    print(i)
    for j in range(0,len(resurl)):
        if j % 2 ==0:
            two = resurl[j+1]
            #f.write(resurl[j] + '\t'+ two[5:8] + '\t' + two[9:-2])
            with open('D:/python/july/data/优书网1.txt', 'a', encoding='utf-8') as file:
                file.write(resurl[j] + '\t'+ two[5:8] + '\t' + two[9:-2] + '\n')