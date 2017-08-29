'''
Created on 2017年6月14日

@author: syl
'''
from selenium import webdriver
from time import sleep
from Logcase.Loginport login

driver=webdriver.Chrome()
driver.get("http://192.168.133.217")
driver.implicitly_wait(10)
driver.maximize_window()
              
main_windows=driver.current_window_handle
              
login().userlogin(driver,13777559149,1234567)   
                        
driver.find_element_by_class_name("go-user-page").click()
sleep(5)
all_handles=driver.window_handles
for handle in all_handles:
    if handle !=main_windows:
        driver.switch_to.window(handle)  
        sleep(5)
driver.find_element_by_class_name("my-video-li").click()
sleep(5) 
s=driver.find_elements_by_xpath("//div[@data-live-name='新建一个直播']")
for i in s:
 print (i.get_attribute("data-live-id"))
          
driver.quit()