import requests, os
import time
#import telegram
from selenium import webdriver
from pymongo import MongoClient

client = MongoClient('mongodb://dridy:1234@ds013475.mlab.com:13475/heroku_4s0bvwj7')
db = client.heroku_4s0bvwj7
#url = "http://www.naver.com"
#bot = telegram.Bot(token='530056797:AAGPAKVoZLKtjlbEKoZWPYk6buUOnln_gyc')

#chat_id = bot.getUpdates()[-1].message.chat.id

downloadPath = 'http://humorbook.co.kr/bbs/board.php?bo_table=star&wr_id=' + str(112167)
print(downloadPath)
browser1 = webdriver.PhantomJS()
browser1.implicitly_wait(3)
browser1.get(downloadPath)
elems = browser1.find_elements_by_css_selector('img.img-tag')
title = browser1.find_element_by_tag_name('h1')
print(title.text)
file_data = []
for elem in elems:
    print(elem.text)
    repath = elem.get_attribute('src')
    file_data.append({"src":repath})
    print('Downloading image %s...' % (repath))

print('new')
db.humorbook.insert_one({"imgs":file_data, "title": title.text,"boardId": 112167})
print('complete:'+title.text)
browser1.quit()


 
#for element1 in boardID:
    #print("-", element.text)
    #bdID = element1.text
    #print('element1 %s' % (element1))
# file_data = []
# with open(os.path.join(BASE_DIR,'latest.txt'),'r+') as f_read:
#     before = f_read.readline()
#     if before != siteID:
#         #bot.sendMessage(chat_id = chat_id, text ='new')
#         downloadPath = 'http://humorbook.co.kr/bbs/board.php?bo_table=star&wr_id=' + str(siteID)
#         print(downloadPath)
#         browser1 = webdriver.PhantomJS()
#         browser1.implicitly_wait(3)
#         browser1.get(downloadPath)
#         browser1.save_screenshot("website.png")
#         elems = browser1.find_elements_by_css_selector('img.img-tag')
#         title = browser1.find_element_by_tag_name('h1')
#         print(title.text)
#         for elem in elems:
#             print(elem.text)
#             repath = elem.get_attribute('src')
#             file_data.append({"src":repath})
#             print('Downloading image %s...' % (repath))

#         print('new')
#         db.humorbook.insert_one({"imgs":file_data, "title": title.text,"id": siteID})
#         print('complete:'+title.text)
#         browser1.quit()
#     else:
#         print('not new')
#         #bot.sendMessage(chat_id = chat_id, text ='not new')
#     f_read.close()

# with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f:
#     f.write(element.text)
#     f.close()


#browser.save_screenshot("website.png")
#for element in element_id:
#   print("-", element.text)
#browser.quit()