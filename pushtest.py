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

message = inputText
message_body1 = ''
result = push_service.notify_single_device( registration_id = registration_id1, message_title = message, message_body = message_body1 )