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
#url = "http://www.naver.com"
#bot = telegram.Bot(token='530056797:AAGPAKVoZLKtjlbEKoZWPYk6buUOnln_gyc')

#chat_id = bot.getUpdates()[-1].message.chat.id

path = 'https://www.pinterest.co.kr/'
#pin/773211829745905053/

browser = webdriver.PhantomJS()

browser.implicitly_wait(1)

browser.get(path)

time.sleep(2)
input_id = browser.find_element_by_name("id")
input_id.clear()
input_id.send_keys('dridy87@naver.com')
input_pw = browser.find_element_by_name("password")
input_pw.clear()
input_pw.send_keys('!@#$56')
# browser.execute_script('frmCheck_auth()')

login_button = browser.find_element_by_css_selector("button.SignupButton")
login_button.submit()

time.sleep(3)

sourceLink = 'https://www.pinterest.co.kr/pin/773211829745905066/'

browser.get(sourceLink)

aTag = browser.find_element_by_css_selector('a.imageLink')

href = aTag.get_attribute('href')
print(href)
title = href.split('/')[-1]
print(title)
imgs = aTag.find_elements_by_css_selector('img')
print(imgs[1].get_attribute('src'))
# for e in imgs:
#     print(e.get_attribute('src'))
    
