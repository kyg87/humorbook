import requests, os
import time
#import telegram
from selenium import webdriver
from pymongo import MongoClient
from pyfcm import FCMNotification


push_service = FCMNotification(api_key="AIzaSyAeG8serpElJCe7URp2ab3liN0IBMqlTAA")

registration_id1 = 'c4SG6Ll1A4w:APA91bGc9_5htDcgbDNikIfG3JMbMU8By8exeWfJvzgjruNJh7V8-86TnhPxYPcZxWHg9eYiOaYqgPyYtlsnjxaxZUl2LFPZbA1MYxq-AXSf6TVCO4qEPAIV9CccRXxqF8ZvQtno8CjI'


client = MongoClient('mongodb://dridy:fkawk1@ds121906.mlab.com:21906/danang')
db = client.danang

path = 'http://www.filejo.com/main/friend2.php?Nicid=0a190a19i9191a190a190a19j619i619a619i6198719e619'

browser = webdriver.PhantomJS()

browser.implicitly_wait(3)

browser.get(path)

input_id = browser.find_element_by_name("mb_id")
input_id.clear()
input_id.send_keys('dridy')
input_pw = browser.find_element_by_name("mb_pw")
input_pw.clear()
input_pw.send_keys('fkawk11')
browser.execute_script('frmCheck_auth()')
time.sleep(1)
browser.get(path)
trs = browser.find_elements_by_css_selector("form[name='frd'] > table > tbody > tr:nth-child(3) > td > table > tbody > tr:nth-child(1) > td >  table > tbody > tr")
browser.save_screenshot("website.png")
for idx,e in enumerate(trs,0):
        if idx % 2 == 1:
            continue
        # print('-',idx)
        title = e.find_element_by_css_selector('td > table > tbody > tr > td:nth-child(2) > a > b > span')
        
        database = db.filejo.find_one({'title':title.text})

        if database != None:
            continue
        print(title.text)
        imgSrc = e.find_element_by_css_selector('td > table > tbody > tr > td:nth-child(1) > div:nth-child(2) a > img')
        temp = (imgSrc.get_attribute('src'))
        print(temp)
        db.filejo.insert_one({ "title":title.text, "imgSrc": temp })

        message = title.text
        message_body1 = ''
        result = push_service.notify_single_device( registration_id = registration_id1, message_title = message, message_body = message_body1 )

browser.quit()