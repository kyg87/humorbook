from selenium import webdriver
import os
import time
import random
import requests
from pymongo import MongoClient
 
client = MongoClient('mongodb://dridy:fkawk1@ds121906.mlab.com:21906/danang')
db = client.danang 

link = 'https://scontent-icn1-1.cdninstagram.com/vp/426deee283309ec3ae0460416e335b69/5A9D43FD/t50.2886-16/26683346_732746310250721_2018781242123616256_n.mp4'
file_name = link.split('/')[-1]

print(file_name)

r = requests.get(link,stream = True)

with open(file_name,'wb') as f:
    for chunk in r.iter_content(chunk_size= 1024*1024):
        if chunk:
            f.write(chunk)
# print("% downloaded!\n" %file_name)

