import requests, os
import time
#import telegram
from selenium import webdriver
from pymongo import MongoClient
from pyfcm import FCMNotification


push_service = FCMNotification(api_key="AIzaSyAeG8serpElJCe7URp2ab3liN0IBMqlTAA")

registration_id1 = 'dV_zajKmr8Y:APA91bFHtuH2YU3eTplSqDSDtSbwXuxq__n__EfHpRMPbwe2FSGXMdjG8giZ-mgE9_9HWVtGvBkiYq6YKX1dr9ivtDJYwxMCNCI2N5i1D0EC69Py_3JUQfxX9ybfG_7U7g5FIdNwXsoz'


client = MongoClient('mongodb://dridy:1234@ds013475.mlab.com:13475/heroku_4s0bvwj7')
db = client.heroku_4s0bvwj7

path = 'http://www.e-pass.co.kr/event/new.asp'

browser = webdriver.PhantomJS()

browser.implicitly_wait(3)

browser.get(path)

element_id = browser.find_elements_by_css_selector('td > a > div')

for idx,e in enumerate(element_id, 0):
    print(idx)
    if idx > 30 :
        continue
    print(e.text)