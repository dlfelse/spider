import time

import requests
requests.adapters.DEFAULT_RETRIES = 5
from base import tool
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
link = 'https://4archive.org/board/hc/thread/1156298/unwanted-unhappy-facial-thread#p1156298'
pageurl = tool.getTarget(link,'//div/div[2]/div[3]/div/a[1]/@href')
i=0
for u in pageurl:
    tool.writetotxt('jp.txt',u)
    tool.downPhoto(u, 'F:\shy\不想\ ', str(time.time()))