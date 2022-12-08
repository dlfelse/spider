import requests
requests.adapters.DEFAULT_RETRIES = 5
from base import tool
import importlib,sys

importlib.reload(sys)
link = 'https://bunkr.is/a/GTxpph19'
# /html/body/div[1]/section/div/div//*/div[2]/p[1]/text() |
# pageurl = tool.getTarget(link,'/html/body/div[1]/section/div/div/div[2]/div[1]/a/text()')
pageurl = tool.getTarget(link,'/html/body/div[1]/section/div/div//*/div[2]/p[1]/text() ')
i=0
for u in pageurl:
    print(u)