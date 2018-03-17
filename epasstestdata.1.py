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

# path = 'http://www.e-pass.co.kr/event/new.asp'


# html = requests.get(path)
# soup = BeautifulSoup(html.content, 'html.parser', from_encoding='utf-8')
# tag_list = soup.find_all('tr',{"height":28})

href = 'new_info.asp?Posi=Home&AdType=Tag&Mode=Event&SMode=New&Cmd=&S_Year=&S_Month=&S_Day=&Page=1&InNo=2018-02-14-120&MF=0&L_URL=/event/new.asp&D_URL=/event/new_info.asp&ApplyChk='
# 14-120
print(href)

downloadPaht = 'http://www.e-pass.co.kr/event/'+ href

browser = webdriver.PhantomJS()

browser.implicitly_wait(3)

browser.get(downloadPaht)
browser.save_screenshot("website.png")

# html body center table tbody tr td font form
#formtag = browser.find_elements_by_css_selector('table > tbody > tr > td > font > form')
formtag = browser.find_elements_by_css_selector("form[name='frm_form'] > table")
table = formtag[1].find_element_by_css_selector("tbody > tr > td > table:nth-child(1)")

print(table.text)

table1 = formtag[1].find_elements_by_css_selector("tbody > tr > td > table")[1]

trs = table1.find_elements_by_css_selector("tbody > tr")

for idx,e in enumerate(trs,0):
    print('-',idx)
    tds = e.find_elements_by_css_selector('td')
    for idx,ab in enumerate(tds,0):
    #     d
        # print(tds[idx].text.strip())
    #    print(tds[idx].text)
        
        if idx >= 1 :
            continue
        if tds[0].text.strip() == "응모대상":
            print(tds[1].text.strip())
        elif tds[0].text.strip() == "행사내용":
            print(tds[1].text.strip())
        elif tds[0].text.strip() == "경품":
            trs2 = tds[1].find_elements_by_css_selector("table > tbody > tr")

            for idx,aaab in enumerate(trs2, 0):
                if idx == 0:
                    continue
                item = aaab.find_element_by_css_selector("td:nth-child(2)")
                count = aaab.find_element_by_css_selector("td:nth-child(3)")
                print(item.text + "/" + count.text)
            # print(tds[1].text.strip())
        elif tds[0].text.strip() == "퀴즈":
            trs2 = tds[1].find_elements_by_css_selector("table > tbody > tr")

            for idx,aaab in enumerate(trs2, 0):
                if idx == 0:
                    continue
                item = aaab.find_element_by_css_selector("td:nth-child(2)")
                count = aaab.find_element_by_css_selector("td:nth-child(3)")
                print(item.text + "/" + count.text)
        elif tds[0].text.strip() == "당첨발표":
            print(tds[1].text.strip())
        elif tds[0].text.strip() == "발표방법":
            print(tds[1].text.strip())
        elif tds[0].text.strip() == "행사내용":
            print(tds[1].text.strip())
        elif tds[0].text.strip() == "주최사":
            print(tds[1].text.strip())


# for idx,e in enumerate(table1,0):
#     print('-',idx)
#     print(e.text)
#print(formtag)
# table = formtag[0].find_elements_by_css_selector('')

javascript_a = formtag[2].find_elements_by_css_selector("tbody > tr:nth-child(3)")

javascript_b = formtag[2].find_element_by_css_selector("td > table > tbody > tr > td > a").get_attribute('href')
print('javascript_b: ' , javascript_b)
# for idx,e in enumerate(javascript_b,0):
#     print('-',idx)
#     print(e)

# for idx,e in enumerate(formtag,0):
#     print('-',idx)
#     print(e.text)


#print(table.text)

#td = table.find_elements_by_css_selector('tr > td:nth-child(2)')

# for idx,e in enumerate(td,0):
#     print('-',idx)
#     print(e.text)
    # print(e.text.replace("\t",""))
    # if(e.text == "경품"):
    #     print('경품')
# print(table[4].text)
# print(table)
# # for idx,e in enumerate(table,0):
# #     print('-',idx)
# #     print(e.text)

# for e in table:
#     print(e)
print(len(browser.window_handles))

browser.execute_script(javascript_b)

print(len(browser.window_handles))

if(len(browser.window_handles) == 3):
    print('handle' , 2)
    browser.switch_to_window(browser.window_handles[1])
else :
    print('handle' , 1)
    
    browser.switch_to_window(browser.window_handles[1])


time.sleep(2)    
# print(browser.window_handles[1])
print(browser.current_url)
browser.quit()

# for idx,e in enumerate(element_id, 0):
#     print(idx)
#     if idx > 30 :
#         continue
#     print(e.text)