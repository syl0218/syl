'''
Created on 2017年6月19日

@author: syl
'''
from selenium import webdriver
import time
import smtplib
from case.Login import  login
from case.NewLive import NewaLive
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://192.168.133.217")
driver.implicitly_wait(10)
login().userlogin(driver, 13777559149, 1234567)
main_windows=driver.current_window_handle
NewaLive().newalive(driver)
all_handles=driver.window_handles
for handle in all_handles:
        if handle !=main_windows:
         driver.switch_to.window(handle)
driver.find_element_by_class_name("deleted").click()

driver.find_element_by_class_name("btn-primary").click()
time.sleep(5)
driver.find_element_by_class_name("btn-primary").click() 
driver.quit()        
         


