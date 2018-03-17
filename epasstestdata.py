import requests, os
import time
#import telegram
from selenium import webdriver
from pymongo import MongoClient
from pyfcm import FCMNotification
from bs4 import BeautifulSoup


push_service = FCMNotification(api_key="AIzaSyAeG8serpElJCe7URp2ab3liN0IBMqlTAA")

registration_id1 = 'dV_zajKmr8Y:APA91bFHtuH2YU3eTplSqDSDtSbwXuxq__n__EfHpRMPbwe2FSGXMdjG8giZ-mgE9_9HWVtGvBkiYq6YKX1dr9ivtDJYwxMCNCI2N5i1D0EC69Py_3JUQfxX9ybfG_7U7g5FIdNwXsoz'


client = MongoClient('mongodb://dridy:1234@ds013475.mlab.com:13475/heroku_4s0bvwj7')
db = client.heroku_4s0bvwj7

path = 'http://www.e-pass.co.kr/event/new.asp'


html = requests.get(path)
soup = BeautifulSoup(html.content, 'html.parser', from_encoding='utf-8')
tag_list = soup.find_all('tr',{"height":28})

href = tag_list[0].select('a')[1].get('href')

print(href)

downloadPaht = 'http://www.e-pass.co.kr/event/'+ href

browser = webdriver.PhantomJS()

browser.implicitly_wait(3)

browser.get(downloadPaht)
# html body center table tbody tr td font form
#formtag = browser.find_elements_by_css_selector('table > tbody > tr > td > font > form')
formtag = browser.find_elements_by_name('frm_form')

table = formtag[0].find_elements_by_css_selector('table')

print(table[4].text)
# for idx,e in enumerate(table,0):
#     print('-',idx)
#     print(e.text)

# for e in tag_list:
#     print(e)


# for idx,e in enumerate(element_id, 0):
#     print(idx)
#     if idx > 30 :
#         continue
#     print(e.text)