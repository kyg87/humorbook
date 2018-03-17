from selenium import webdriver
import os
import time
import random
import sys
from pymongo import MongoClient
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyAeG8serpElJCe7URp2ab3liN0IBMqlTAA")

registration_id1 = 'c4SG6Ll1A4w:APA91bGc9_5htDcgbDNikIfG3JMbMU8By8exeWfJvzgjruNJh7V8-86TnhPxYPcZxWHg9eYiOaYqgPyYtlsnjxaxZUl2LFPZbA1MYxq-AXSf6TVCO4qEPAIV9CccRXxqF8ZvQtno8CjI'

client = MongoClient('mongodb://dridy:fkawk1@ds121906.mlab.com:21906/danang')
db = client.danang 


inputText = ''
for i in range(1,len(sys.argv)):
    inputText = sys.argv[i]
print(inputText)

def listVideos(driver):
    # type: (webdriver) -> list(str)
    
    results = set()

    videos = driver.find_elements_by_xpath("//div[@class='_mck9w _gvoze _tn0ps']/a")
    for video in videos:
        videoLink = video.get_attribute('href')
        # print ('find video', videoLink)
        if videoLink not in results:
            database = db.he.le.n_.find_one({'videoLink':videoLink})
            if database != None:
                continue
            results.add(videoLink)
            print ('find video', videoLink)

    # As Instagram uses dynamic loads more video, thus we need to scroll down the page to find more videos.

    return results
 
 
def getVideo(driver, videoLink):

    browser1 = webdriver.PhantomJS()
    browser1.implicitly_wait(1)
    
    browser1.get(videoLink)
    
    lis = browser1.find_elements_by_class_name('_ezgzd')

    try:
        title = lis[0].find_element_by_css_selector('span > span').text
    except:
        title = ''

    file_data = []
    mp4 =''
    try:
        tt = browser1.find_element_by_css_selector('video._l6uaz')
        mp4 = tt.get_attribute('src')

    except:
        try:
            while True:
                elems = browser1.find_elements_by_css_selector('img._2di5p')
                for idx,elem in enumerate(elems,0):
                    print('-',idx)
                    repath = elem.get_attribute('src')
                    file_data.append({"src":repath})
                    print('Downloading image %s...' % (repath))

                buttonR = browser1.find_element_by_class_name('coreSpriteRightChevron')
                print('is',buttonR.text)
                buttonR.click()
                browser1.implicitly_wait(1)
        except:
            print('none')
    
    db.he.le.n_.insert_one({'instaId' :inputText,"imgs":file_data, "title": title,'mp4':mp4,'videoLink':videoLink})
    print('complete:'+videoLink)
    message = inputText
    message_body1 = title
    result = push_service.notify_single_device( registration_id = registration_id1, message_title = message, message_body = message_body1 )
    print(result)

def checkVideoDurationSeconds():
    # type: () -> None
    
    for video in os.listdir(os.curdir):
        if not video.endswith("mp4"):
            continue
        print (video)
        os.system('ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(os.path.join(os.curdir, video)))
 
 
def main():
    print('-',os.curdir)
    sourceLink = 'https://www.instagram.com/'+ inputText +'/'
    #sourceLink = 'https://www.instagram.com/j.caeyul/'
    driver = webdriver.PhantomJS()
    driver.get(sourceLink)
    videoLinks = listVideos(driver)
    print ('get {} number of videos'.format(len(videoLinks)))
    for videoLink in videoLinks:
        print ('download', videoLink)
        getVideo(driver, videoLink)
        time.sleep(random.randint(10, 30))
    driver.close()
    checkVideoDurationSeconds()
 
 
if __name__ == "__main__":
    main()