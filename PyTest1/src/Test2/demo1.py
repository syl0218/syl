'''
Created on 2017年5月19日

@author: syl
'''
# coding:utf-8

from selenium import webdriver
from time import *

driver = webdriver.Chrome()

driver.get("http://www.qlmzhibo.com")

#driver.maximize_window()

h = driver.current_window_handle

print (h)  # 打印首页句柄
print(driver.title)

sleep(10)
driver.find_element_by_class_name("check_login_start").click()
sleep(2)
driver.find_element_by_name("username").send_keys("13777559149")
sleep(2)
driver.find_element_by_name("password").send_keys("1234567")
sleep(2)
driver.find_element_by_class_name("btn-login-submit").click()

sleep(2)
driver.find_element_by_class_name("go-user-page").click()


all_h = driver.window_handles

print (all_h)   
# 方法二：获取list里面第二个直接切换

driver.switch_to.window(all_h[1])

print (driver.title)

# 关闭新窗口

driver.close()

# 切换到首页句柄

driver.switch_to.window(h)

# 打印当前的title

print (driver.title)

driver.quit()