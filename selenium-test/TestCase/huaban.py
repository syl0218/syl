'''
Created on 2017年8月28日

@author: syl
'''
from selenium import webdriver
from time import sleep


class huaban():
   driver=webdriver.Chrome()
   driver.get("http://huaban.com")
   driver.find_element_by_id("query").send_keys("tiantian")
   sleep(4)
   driver.find_element_by_class_name("go").click()
   sleep(10)
   driver.quit()