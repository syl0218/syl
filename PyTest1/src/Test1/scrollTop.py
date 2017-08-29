'''
Created on 2016年12月20日

@author: syl
'''
from selenium import webdriver
from time import *
 


driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(5)
js = "var q=document.body.scrollTop=10000"
js2="window.scrollTo(1,document.body.scrollHeight)"
driver.execute_script(js2)
sleep(5)
driver.quit()  


