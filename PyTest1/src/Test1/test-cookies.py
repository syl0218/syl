'''
Created on 2017年6月16日

@author: syl
'''
from selenium import webdriver
import time
from Login import login
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome()
driver.get("http://www.qlmzhibo.com")
#print (driver.get_cookies())
#login().userlogin(driver,13777559149,1234567) 
print (driver.get_cookies())
#  cookie 要抓包获取  全部信息
c1={ 'domain': 'www.qlmzhibo.com', 
     'httpOnly': False, 
     'name': '__fpgid', 
     'path': '/', 
     'secure': False,
     'value': '_564b4523294e61feef405da662f4e3a9'}
c2={ 'domain': 'www.qlmzhibo.com',
     'expiry': 1498227109.554524,
     'httpOnly': True, 
     'name': 'SHIROJSID', 
     'path': '/', 
     'secure': False,
     'value': '04b12d60-200b-4a93-ba8d-253fe45d01a6'}

c3={ 'domain': 'www.qlmzhibo.com', 
     'expiry':"1498227118.153642", 
     'httpOnly': True, 
     'name': 'access_token',
     'path': '/', 'secure': False, 
     'value': '791153c2b168394671f028c6089fdb87'}
driver.delete_all_cookies()
driver.add_cookie(c1)
driver.add_cookie(c2)
#login().userlogout(driver)
driver.add_cookie(c3)

time.sleep(3)
driver.refresh()
print (driver.get_cookies())
time.sleep(30)
driver.quit()