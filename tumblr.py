from selenium import webdriver
import os
import time
import random
import sys
from pymongo import MongoClient
 
client = MongoClient('mongodb://dridy:fkawk1@ds121906.mlab.com:21906/danang')
db = client.danang 

database = db.instaId.find_one({'instaId':'hatsuneyuko'})
if database == None:
    db.instaId.insert_one({'instaId' :'hatsuneyuko'})


def listVideos(driver):
    # type: (webdriver) -> list(str)
    
    results = set()
    while True:
        newVideoFound = False
        iframes = driver.find_elements_by_css_selector('iframe.photoset')

        # videos = iframes.find_elements_by_css_selector('div.photoset_row')
        
        
        # print(len(iframes))
        for video in iframes:
            videoLink = video.get_attribute('src')
            # print ('find video', videoLink)
            if videoLink not in results:
                results.add(videoLink)
                print ('find video', videoLink)
                newVideoFound = True
        if not newVideoFound:
            break
        # As Instagram uses dynamic loads more video, thus we need to scroll down the page to find more videos.
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        time.sleep(1)
        
        
    return results
 
 
def getVideo(driver, videoLink):
    # type: (webdriver, str) -> None
    # driver.implicitly_wait(3)


    browser1 = webdriver.PhantomJS()
    browser1.implicitly_wait(1)
    

    browser1.get(videoLink)

    title =''
    file_data = []
    imgs = browser1.find_elements_by_css_selector('div.photoset_row > a')
    temp = browser1.find_element_by_css_selector('div.photoset_row > a > img').get_attribute('data-pin-url')
    title = temp.split('/')[-1]
    print(title)
    for e in imgs:
        file_data.append({"src":e.get_attribute('href')})
        print(e.get_attribute('href'))
    
    db.he.le.n_.insert_one({'instaId' :'hatsuneyuko','imgs':file_data, 'title': title,'mp4':'','videoLink':videoLink})
    print('complete:'+videoLink)
    browser1.quit()

    

    # buttonR.click()h
    

    

 
def checkVideoDurationSeconds():
    # type: () -> None
    
    for video in os.listdir(os.curdir):
        if not video.endswith("mp4"):
            continue
        print (video)
        os.system('ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(os.path.join(os.curdir, video)))
 
 
def main():
    print('-',os.curdir)
    #sourceLink = 'https://www.instagram.com/he.le.n_/'
    #sourceLink = 'https://www.instagram.com/j.caeyul/'
    sourceLink = 'https://hatsuneyuko.tumblr.com'
    driver = webdriver.PhantomJS()
    driver.implicitly_wait(1)
    
    driver.get(sourceLink)
    
    videoLinks = listVideos(driver)
    print ('get {} number of videos'.format(len(videoLinks)))
    for videoLink in videoLinks:
        print ('download', videoLink)
        getVideo(driver, videoLink)
        time.sleep(random.randint(3, 10))
    driver.close()
    #checkVideoDurationSeconds()
    
 
if __name__ == "__main__":
    main()