import requests, os
import time
#import telegram
from selenium import webdriver
from pymongo import MongoClient
from pyfcm import FCMNotification
from bs4 import BeautifulSoup


push_service = FCMNotification(api_key="AIzaSyAeG8serpElJCe7URp2ab3liN0IBMqlTAA")

registration_id1 = 'dV_zajKmr8Y:APA91bFHtuH2YU3eTplSqDSDtSbwXuxq__n__EfHpRMPbwe2FSGXMdjG8giZ-mgE9_9HWVtGvBkiYq6YKX1dr9ivtDJYwxMCNCI2N5i1D0EC69Py_3JUQfxX9ybfG_7U7g5FIdNwXsoz'


client = MongoClient('mongodb://dridy:fkawk1@ds121906.mlab.com:21906/danang')
db = client.danang

path = 'http://www.e-pass.co.kr/event/new.asp'


browser = webdriver.PhantomJS()

browser.implicitly_wait(3)

browser.get(path)

formtag = browser.find_elements_by_css_selector("form[name='frm_form'] > table")

tds = formtag[5].find_elements_by_css_selector('tr')

for idx,aa in enumerate(tds,0):
    if idx % 4 ==0:
        # print('-----------------------------------',idx)
        td = aa.find_elements_by_css_selector('td')
        
        print(td[7].text)
        print(td[8].text)

# for idx,aa in enumerate(tds,0):
#     # if idx % 2 ==0:
#         print(idx % 2)

td = tds[0].find_elements_by_css_selector('td')

t = td[7]

print('title',t.text)

dt = td[8]

print('dt',dt.text)

title = browser.find_elements_by_css_selector("div[title]")


