'''
Created on 2017年7月11日

@author: syl
'''
from selenium import webdriver
import sys
from time import sleep
from threading import Thread
from fengzhuang import syl

def test_baidu_search(browser,url):
    '''driver=None
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    if driver==None:
        exit()
    '''    
    driver=syl(browser)
    driver.get(url)
    sleep(3)
    kw=("id","kw")
    su=("id","su")
    
    driver.send_keys(kw,"123")   
    driver.click(su)
    sleep(4)
    driver.quit()
if __name__ =="__main__" :       
        
 data={"chrome":"http://www.baidu.com",
       "firefox":"http://www.baidu.com"
          }
    
 Threads=[]
 for b,url in data.items():
        t=Thread(target=test_baidu_search,args=(b,url))        
        Threads.append(t)
        
 for thr in Threads:
    thr.start()  
        
        
        