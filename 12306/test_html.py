import urllib
from bs4 import BeautifulSoup
from xlwt import *  
import json
import time 
import random
import re

htmlfile = open('test.html', 'r', encoding='utf-8')
htmlhandle = htmlfile.read()



#jd = json.loads(htmlhandle.text.strip('var ticketInfoForPassengerForm='))

# pattern = re.compile(r"leftTicketStr", re.MULTILINE | re.DOTALL)
# a1 = re.search(r'queryLeftTicketRequestDTO\':([\s\S]*?);', htmlhandle).group()

# a2 = re.search(r'ypInfoDetail\':\'([\s\S]*?)\'', a1).group()
# a3 = re.search(r'train_location\':\'([\s\S]*?)\'', a1).group()
# ypInfoDetail = re.sub(r'(ypInfoDetail)|(,)|(\s)|(;)|(\')|(:)', '', a2)
# train_location = re.sub(r'(train_location)|(,)|(\s)|(;)|(\')|(:)', '', a3)
# print(ypInfoDetail)
# print(train_location)

a1 = re.search(r'key_check_isChange\':\'([\s\S]*?)\'', htmlhandle).group()
key_check_isChange = re.sub(r'(key_check_isChange)|(,)|(\s)|(;)|(\')|(:)', '', a1)
print(key_check_isChange)
#print(pattern.search(script.text).group(1))
