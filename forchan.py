import time
import you_get
import requests
requests.adapters.DEFAULT_RETRIES = 5
from base import tool
import importlib,sys
from multiprocessing.dummy import Pool as ThreadPool
importlib.reload(sys)
link = 'https://boards.4chan.org/gif/thread/19321612'
pageurl = tool.getTarget(link,'//div/a/@href')
i=0
path = 'F:\shy\Hegre\ '
for u in pageurl:
    tool.writetotxt('jp.txt','https:' + u)
    i = i + 1
    if i%2 == 0:
        if u.endswith('.gif'):
            print('this is a gif')
            tool.downGif('https:' + u, path, str(time.time()))
        elif u.endswith('.webm'):
            print('this is a web')
            tool.downVideo('https:' + u,path)
            # directory = r''  # 设置下载目录
            # sys.argv = ['you-get','-o', directory, uy]  # sys传递参数执行下载，就像在命令行一样
            # you_get.main()
        # tool.downPhoto('https:' + u, 'F:\shy\gif\ ', str(time.time()))
        else:
            tool.downPhoto('https:' + u, path, str(time.time()))