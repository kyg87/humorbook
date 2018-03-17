import requests, os
import time
from selenium import webdriver
from pymongo import MongoClient
from pyfcm import FCMNotification


push_service = FCMNotification(api_key="AIzaSyAeG8serpElJCe7URp2ab3liN0IBMqlTAA")

registration_id1 = 'dV_zajKmr8Y:APA91bFHtuH2YU3eTplSqDSDtSbwXuxq__n__EfHpRMPbwe2FSGXMdjG8giZ-mgE9_9HWVtGvBkiYq6YKX1dr9ivtDJYwxMCNCI2N5i1D0EC69Py_3JUQfxX9ybfG_7U7g5FIdNwXsoz'

message = "test"
message_body1 ="hi"
result = push_service.notify_single_device(registration_id=registration_id1,message_title=message,message_body=message_body1)

print(result)