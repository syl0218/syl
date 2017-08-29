'''
Created on 2017年6月23日

@author: syl
'''
from selenium import webdriver
import re

driver=webdriver.Chrome()
driver.get("http://www.cnblogs.com/yoyoketang/")
page=driver.page_source
url_list=re.findall('href=\"(.*?)\"',page)
print (page)
url_all=[]
for url in url_list:
    if "http" in url:
        #print (url)
        url_all.append(url)       
#print (url_all)
driver.quit()
