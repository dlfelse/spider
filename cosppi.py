# coding=utf-8
#下载avmoo网站中的AV剧情截图
import requests
requests.adapters.DEFAULT_RETRIES = 5
from base import tool
import importlib,sys
importlib.reload(sys)
#全部作品页数,注意网址后缀可能有变化
alllink = tool.getAllPages('https://cosppi.net/sort/follower-rank/page/',1,23)


for link in alllink:
    pageurl = tool.getTarget(link,'/html/body/div[1]/div[3]/div/main/article/div/div[4]/div[1]/a/div[2]/a/@href')
    for u in pageurl:
        #后续变化中缺少了前缀
        picurl = tool.getTarget('https:' + u,'/html/body/div[2]/div[7]//a/@href')
        for p in picurl:
            #从链接中提取番号作为名称
            prename = p.split('/')[-1][:-4] + ' '
            tool.writetotxt('../data/uuu.txt', prename + p)