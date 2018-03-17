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

path = 'https://www.instagram.com/accounts/login/'

browser = webdriver.PhantomJS()

browser.implicitly_wait(3)

browser.get(path)

input_id = browser.find_element_by_name("username")
input_id.clear()
input_id.send_keys('dridy@naver.com')
input_pw = browser.find_element_by_name("password")
input_pw.clear()
input_pw.send_keys('!@#$ebsi57203927')
# browser.execute_script('frmCheck_auth()')

login_button = browser.find_elements_by_css_selector("button")

for  e in login_button:
    print(e.text)
    e.submit()

time.sleep(2)
# login_button.submit()
browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
time.sleep(1)
browser.save_screenshot("website.png")

