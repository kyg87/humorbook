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

lastDay = ''

for idx,aa in enumerate(tds,0):
    if idx % 4 ==0:
        # print('-----------------------------------',idx)
        td = aa.find_elements_by_css_selector('td')
        
        print(td[7].text)
        title = td[7].text

        database = db.event.find_one({'title':title})

        if database != None:
            continue

        href = td[7].find_element_by_tag_name('a').get_attribute('href') 
       
        downloadPaht =  href

        print(downloadPaht)

        browser1 = webdriver.PhantomJS()

        browser1.implicitly_wait(3)

        browser1.get(downloadPaht)

        formtag = browser1.find_elements_by_css_selector("form[name='frm_form'] > table")
        table = formtag[1].find_element_by_css_selector("tbody > tr > td > table:nth-child(1)")

        # print(table.text)

        table1 = formtag[1].find_elements_by_css_selector("tbody > tr > td > table")[1]

        trs = table1.find_elements_by_css_selector("tbody > tr")
        
        target = ''
        caption = ''
        gift = []
        quiz = []
        notiType = ''
        winday =''
        crop = ''
        for idx,e in enumerate(trs,0):
            tds = e.find_elements_by_css_selector('td')
            for idx,ab in enumerate(tds,0):
                
                if idx >= 1 :
                    continue
                if tds[0].text.strip() == "응모대상":
                    print(tds[1].text.strip())
                    target = tds[1].text.strip()
                elif tds[0].text.strip() == "행사내용":
                    print(tds[1].text.strip())
                    caption = tds[1].text.strip()
                elif tds[0].text.strip() == "경품":
                    trs2 = tds[1].find_elements_by_css_selector("table > tbody > tr")
                    
                    for idx,aaab in enumerate(trs2, 0):
                        if idx == 0:
                            continue
                        item = aaab.find_element_by_css_selector("td:nth-child(2)")
                        count = aaab.find_element_by_css_selector("td:nth-child(3)")
                        gift.append({"item":item.text,"count":count.text})
                        
                    # print(tds[1].text.strip())
                elif tds[0].text.strip() == "퀴즈":
                    trs2 = tds[1].find_elements_by_css_selector("table > tbody > tr")

                    for idx,aaab in enumerate(trs2, 0):
                        if idx == 0:
                            continue
                        item = aaab.find_element_by_css_selector("td:nth-child(2)")
                        count = aaab.find_element_by_css_selector("td:nth-child(3)")
                        quiz.append({"item":item.text,"count":count.text})
                elif tds[0].text.strip() == "당첨발표":
                    print(tds[1].text.strip())
                    winday = tds[1].text.strip()
                elif tds[0].text.strip() == "발표방법":
                    print(tds[1].text.strip())
                    notiType = tds[1].text.strip()
                elif tds[0].text.strip() == "주최사":
                    print(tds[1].text.strip())
                    crop = tds[1].text.strip()

        javascript_b = formtag[2].find_element_by_css_selector("td > table > tbody > tr > td > a").get_attribute('href')

        browser1.execute_script(javascript_b)


        if(len(browser.window_handles) == 3):
            browser1.switch_to_window(browser1.window_handles[1])
        else :
            browser1.switch_to_window(browser1.window_handles[1])

        lastDay = td[8].text
        time.sleep(2)    
        # print(browser.window_handles[1])
        
        url = browser.current_url
        print(gift)
        print(quiz)
        #db.event.insert_one({ "title":title, "caption":caption, "target":target, "crop":crop, "lastDay":lastDay, "winday":winday, "gift":gift, "quiz":quiz, "url":url  })
        db.event.insert_one({ "title":title, "caption":caption, "target":target, "crop":crop, "lastDay":lastDay, "winday":winday, "gift":gift, "quiz":quiz, "url":url  })

        message = title
        message_body1 = caption
        result = push_service.notify_single_device( registration_id = registration_id1, message_title = message, message_body = message_body1 )
        
message = '1hour'
message_body1 = 'caption'
result = push_service.notify_single_device( registration_id = registration_id1, message_title = message, message_body = message_body1 )
