from selenium import webdriver
import os
import time
import random
import sys
from pymongo import MongoClient
 
client = MongoClient('mongodb://dridy:fkawk1@ds121906.mlab.com:21906/danang')
db = client.danang 

database = db.instaId.find_one({'instaId':'pinterest'})
if database == None:
    db.instaId.insert_one({'instaId' :'pinterest'})

def listVideos(driver):
    # type: (webdriver) -> list(str)
    
    results = set()
    time.sleep(2)
    while True:
        newVideoFound = False
        videos = driver.find_elements_by_css_selector('div.pinWrapper > div > a')
        for video in videos:
            
            videoLink = video.get_attribute('href')
            # print ('find video', videoLink)
            if videoLink not in results:
                results.add(videoLink)
                print ('find video', videoLink)
                newVideoFound = True
        if not newVideoFound:
            break
        # As Instagram uses dynamic loads more video, thus we need to scroll down the page to find more videos.
        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(3)
    return results
 
 
def getVideo(driver, videoLink):
    # type: (webdriver, str) -> None
    # driver.implicitly_wait(3)

    title = ''

    file_data = []
    mp4 =''

    driver.get(videoLink)

    aTag = driver.find_element_by_css_selector('a.imageLink')

    href = aTag.get_attribute('href')

    title = href.split('/')[-1]

    imgs = aTag.find_elements_by_css_selector('img')

    repath = imgs[1].get_attribute('src')
    file_data.append({"src":repath})
    
    db.he.le.n_.insert_one({'instaId' :'pinterest','imgs':file_data, 'title': title,'mp4':mp4,'videoLink':href})
    print('complete:'+videoLink)


def checkVideoDurationSeconds():
    # type: () -> None
    
    for video in os.listdir(os.curdir):
        if not video.endswith("mp4"):
            continue
        print (video)
        os.system('ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(os.path.join(os.curdir, video)))
 
def logIn(driver):
    path = 'https://www.pinterest.co.kr/'

    driver.implicitly_wait(1)

    driver.get(path)

    time.sleep(2)
    input_id = driver.find_element_by_name("id")
    input_id.clear()
    input_id.send_keys('dridy87@naver.com')
    input_pw = driver.find_element_by_name("password")
    input_pw.clear()
    input_pw.send_keys('!@#$56')
    # browser.execute_script('frmCheck_auth()')

    login_button = driver.find_element_by_css_selector("button.SignupButton")
    login_button.submit()

    time.sleep(3)

def main():
    driver = webdriver.PhantomJS()

    logIn(driver)

    sourceLink = 'https://www.pinterest.co.kr/zkdntm7/pins/'
    driver.implicitly_wait(1)
    driver.get(sourceLink)
    driver.save_screenshot('pin.png')
    videoLinks = listVideos(driver)
    print ('get {} number of videos'.format(len(videoLinks)))
    for videoLink in videoLinks:
        print ('download', videoLink)
        getVideo(driver, videoLink)
        time.sleep(random.randint(3, 10))
    driver.close()
    checkVideoDurationSeconds()
    
 
if __name__ == "__main__":
    main()