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

path = 'http://humorbook.co.kr/bbs/board.php?bo_table=star'

browser = webdriver.PhantomJS()

browser.implicitly_wait(3)

browser.get(path)

element_id = browser.find_elements_by_css_selector("div.table-responsive.list-pc > table > tbody > tr")

trs = browser.find_elements_by_css_selector("div.table-responsive.list-pc > table > tbody > tr > td > span.en")

boardId =''
for idx,e in enumerate( element_id,0):
    if idx == 0 :
        continue
    print(e.find_element_by_css_selector("td > span.en").text)
    boardId = e.find_element_by_css_selector("td > span.en").text
    database = db.star.find_one({'boardId':boardId})
    if database != None:
        continue

    

    href = e.find_element_by_tag_name('a').get_attribute('href')

    print(href)

    browser1 = webdriver.PhantomJS()
    browser1.implicitly_wait(3)
    browser1.get(href)
    elems = browser1.find_elements_by_css_selector('img.img-tag')
    title = browser1.find_element_by_tag_name('h1')
    #print(title.text)
    file_data = []
    for elem in elems:
        print(elem.text)
        repath = elem.get_attribute('src')
        file_data.append({"src":repath})
        print('Downloading image %s...' % (repath))

    db.star.insert_one({"imgs":file_data, "title": title.text,"boardId": boardId})
    print('complete:'+title.text)

    time.sleep(10)  

    notiTitle = title.text
    browser1.quit()

    message = notiTitle
    message_body1 = ''
    result = push_service.notify_single_device( registration_id = registration_id1, message_title = message, message_body = message_body1 )
    print(result)
browser.quit()