'''
Created on 2017年6月29日

@author: syl
'''
#from xml.sax.xmlreader import Locator
u"把get find_element   click   send_keys   封装"


from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait



class fz(object):
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()        
    def get(self,url):       
        self.driver.get(url)        
    def find_element(self,locator,timeout=10):       
        element=WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
        return element    
    def click(self,locator):        
        element=self.find_element(locator)
        element.click()
    def send_keys(self,locator,text):
        element=self.find_element(locator)
        element.clear()
        element.send_keys(text)            
    def quit(self):       
        self.driver.quit()
'''       
if __name__=="__main__":
    d=fz()
    d.get("http://www.baidu.com")
    input_loc=("id","kw")
    d.send_keys(input_loc,"selenium")
    button_loc=("id","su")
    d.click(button_loc)
    d.quit()
'''       
          
        