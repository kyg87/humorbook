import requests, os
import time
import telegram
from selenium import webdriver
from pymongo import MongoClient

#url = "http://www.naver.com"
bot = telegram.Bot(token='530056797:AAGPAKVoZLKtjlbEKoZWPYk6buUOnln_gyc')

chat_id = bot.getUpdates()[-1].message.chat.id

path = 'http://humorbook.co.kr/bbs/board.php?bo_table=star'

browser = webdriver.PhantomJS()

browser.implicitly_wait(3)
while True:
    browser.get(path)

    element_id = browser.find_elements_by_css_selector("div.table-responsive.list-pc > table > tbody > tr")

    #print(element_id)

    siteCurrentID = element_id[1].find_elements_by_css_selector("span.en")

    print(siteCurrentID)

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    #with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_write:

    for element in siteCurrentID:
        #print("-", element.text)
        siteID = element.text

    with open(os.path.join(BASE_DIR,'latest.txt'),'r+') as f_read:
        before = f_read.readline()
        if before != siteID:
            bot.sendMessage(chat_id = chat_id, text ='new')
            print('new')
        else:
            print('not new')
            bot.sendMessage(chat_id = chat_id, text ='not new')
        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f:
        f.write(element.text)
        f.close()
    time.sleep(60)

#browser.save_screenshot("website.png")
#for element in element_id:
#   print("-", element.text)
#browser.quit()