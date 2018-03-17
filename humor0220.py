import requests, os
import time
#import telegram
from selenium import webdriver
from pymongo import MongoClient
from pyfcm import FCMNotification


push_service = FCMNotification(api_key="AIzaSyAeG8serpElJCe7URp2ab3liN0IBMqlTAA")

registration_id1 = 'dV_zajKmr8Y:APA91bFHtuH2YU3eTplSqDSDtSbwXuxq__n__EfHpRMPbwe2FSGXMdjG8giZ-mgE9_9HWVtGvBkiYq6YKX1dr9ivtDJYwxMCNCI2N5i1D0EC69Py_3JUQfxX9ybfG_7U7g5FIdNwXsoz'


client = MongoClient('mongodb://dridy:fkawk1@ds121906.mlab.com:21906/danang')
db = client.danang
#url = "http://www.naver.com"
#bot = telegram.Bot(token='530056797:AAGPAKVoZLKtjlbEKoZWPYk6buUOnln_gyc')

#chat_id = bot.getUpdates()[-1].message.chat.id
while True:
    path = 'http://humorbook.co.kr/bbs/board.php?bo_table=star'

    browser = webdriver.PhantomJS()

    browser.implicitly_wait(3)

    browser.get(path)

    element_id = browser.find_elements_by_css_selector("div.table-responsive.list-pc > table > tbody > tr")

    #print(element_id)

    siteCurrentID = element_id[1].find_elements_by_css_selector("span.en")

    boardID = element_id[1].find_element_by_tag_name('a').get_attribute('href')

    #print(boardID.split('=')[2])

    #print(siteCurrentID)

    siteID = boardID.split('=')[2]
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    database = db.humorbook.find_one({"$query":{},"$orderby":{"_id": -1}})
    before = database['boardId']
    print('before' , before)
    print('current',siteID) 
    
    if int(before) != int(siteID):
        notiTitle =''
        while not int(before) >= int(siteID):
            before = before + 1
            print('before' , before)
            downloadPath = 'http://humorbook.co.kr/bbs/board.php?bo_table=star&wr_id=' + str(before)
            print(downloadPath)
            browser1 = webdriver.PhantomJS()
            browser1.implicitly_wait(3)
            browser1.get(downloadPath)
            elems = browser1.find_elements_by_css_selector('img.img-tag')
            title = browser1.find_element_by_tag_name('h1')
            #print(title.text)
            file_data = []
            for elem in elems:
                print(elem.text)
                repath = elem.get_attribute('src')
                file_data.append({"src":repath})
                print('Downloading image %s...' % (repath))

        
            db.humorbook.insert_one({"imgs":file_data, "title": title.text,"boardId": before})
            print('complete:'+title.text)
            notiTitle = title.text
            browser1.quit()
        print('noti push')
        
        message = notiTitle
        message_body1 = ''
        result = push_service.notify_single_device( registration_id = registration_id1, message_title = message, message_body = message_body1 )
        print(result)
    browser.quit()
    time.sleep(600)

    
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