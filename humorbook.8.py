# -*- coding:utf-8 -*-
import sys
import requests, os
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pymongo import MongoClient

temp = ''
for i in range(1,len(sys.argv)):
    temp = sys.argv[i]
print(temp)


client = MongoClient('mongodb://dridy:fkawk1@ds121906.mlab.com:21906/danang')
db = client.danang

mp4List = db.he.le.n_.find({"instaId":str(temp)})

os.makedirs('E:/'+temp+'/',exist_ok = True)

for key in mp4List:
    if(key['mp4'] == ''):
        link = key['imgs']
        # print(link)
        for e in link:
            repath = e['src']
            file_name = repath.split('/')[-1] 
            print(file_name)
            res = requests.get(repath)
            res.raise_for_status()
            imageFile = open(os.path.join('E:/'+temp+'/',os.path.basename(repath)),'wb')
            for chunk in res.iter_content(10000):
                imageFile.write(chunk)
            imageFile.close()
    else:
        link = key['mp4']
        print(link)
        file_name = link.split('/')[-1] 
        r = requests.get(link, stream = True)

        # download started
        with open(os.path.join('E:/'+temp+'/', os.path.basename(file_name)), 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)
        time.sleep(1)

