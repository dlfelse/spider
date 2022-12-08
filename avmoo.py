# coding=utf-8
#下载avmoo网站中的AV剧情截图
import requests
requests.adapters.DEFAULT_RETRIES = 5
from base import tool
import importlib,sys
importlib.reload(sys)
#女优编号
keyword = 'de606f3b3db16d93'

#全部作品页数,注意网址后缀可能有变化
alllink = tool.getAllPages('https://avmoo.click/cn/star/' + keyword + '/page/',1,2)


for link in alllink:
    pageurl = tool.getTarget(link,'/html/body/div[2]/div/div//div/a/@href')
    for u in pageurl:
        #后续变化中缺少了前缀
        picurl = tool.getTarget('https:' + u,'/html/body/div[2]/div[7]//a/@href')
        for p in picurl:
            #从链接中提取番号作为名称
            prename = p.split('/')[-1][:-4] + ' '
            tool.writetotxt('../data/uuu.txt', prename + p)