from selenium import webdriver
import os
import time
import random

from pymongo import MongoClient
 
client = MongoClient('mongodb://dridy:fkawk1@ds121906.mlab.com:21906/danang')
db = client.danang 

def listVideos(driver):
    # type: (webdriver) -> list(str)
    
    results = set()
    while True:
        newVideoFound = False
        videos = driver.find_elements_by_xpath("//div[@class='_mck9w _gvoze _tn0ps']/a")
        for video in videos:
            videoLink = video.get_attribute('href')
            print ('find video', videoLink)
            if videoLink not in results:
                results.add(videoLink)
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


    browser1 = webdriver.PhantomJS()
    browser1.implicitly_wait(1)
    

    browser1.get(videoLink)
    # start = browser1.page_source.find('"video_url":"')
    # end = browser1.page_source.find('"', start + len('"video_url":"'))
    # sourceLink = browser1.page_source[start + len('"video_url":"'): end]

    # print(sourceLink)
    # os.system("wget --no-check-certificate {}".format(sourceLink))

    file_data = []
    
    try:
        while True:
            elems = browser1.find_elements_by_css_selector('img._2di5p')
            for idx,elem in enumerate(elems,0):
                print('-',idx)
                repath = elem.get_attribute('src')
                file_data.append({"src":repath})
                print('Downloading image %s...' % (repath))

            buttonR = browser1.find_element_by_class_name('coreSpriteRightChevron')
            # buttonR = browser1.find_element_by_css_selector("a._8kphn _by8kl coreSpriteRightChevron")
            print('is',buttonR.text)
            buttonR.click()
            browser1.implicitly_wait(1)
    except:
        print('none')
    
    # db.j.caeyul.insert_one({"imgs":file_data, "title": videoLink})
    print('complete:'+videoLink)

    

    # buttonR.click()h
    

    

 
def checkVideoDurationSeconds():
    # type: () -> None
    
    for video in os.listdir(os.curdir):
        if not video.endswith("mp4"):
            continue
        print (video)
        os.system('ffprobe -i {} -show_entries format=duration -v quiet -of csv="p=0"'.format(os.path.join(os.curdir(), video)))
 
 
def main():
    print('-',os.curdir)
    # sourceLink = 'https://www.instagram.com/he.le.n_/'
    sourceLink = 'https://www.instagram.com/j.caeyul/'
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