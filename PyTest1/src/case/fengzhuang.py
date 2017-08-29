'''
Created on 2017年7月3日

@author: syl
'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class syl(object):

 def __init__(self,browser):
    '''启动浏览器'''
    self.driver=None
    if browser=="chrome":
        self.driver=webdriver.Chrome()
    elif browser=="firefox":
        self.driver=webdriver.Firefox()
    if self.driver==None:
        exit()
    self.driver.implicitly_wait(10)
    self.driver.maximize_window()
 def get(self,url):
     
    self.driver.get(url)
    
 def find_element(self,locator,timeout=10):
    '''定位元素，参数locator是元祖类型'''
    try:
      element=WebDriverWait(self.driver,timeout,5).until(EC.presence_of_element_located(locator))
    except NoSuchElementException as msg:
        print("未定位到该元素"%msg)
    else :
        return element
 def find_elements(self,locator,timeout=10):
    '''定位一组元素，参数locator是元祖类型'''
    elements=WebDriverWait(self.driver,timeout,5).until(EC.presence_of_all_elements_located(locator))
    return elements
 def click(self,locator):
    '''点击操作'''
    
    element=self.find_element(locator)
    element.click()
    
 def right_click(self, element):
    '''鼠标右击''' 
    ActionChains(self.driver).context_click(self.find_element(element)).perform()  
 def double_click(self, element):
    '''鼠标双击''' 
    ActionChains(self.driver).double_click(self.find_element(element)).perform()  
 def send_keys(self,locator,text):
    '''  发送文本输入 '''
    element=self.find_element(locator)
   
    element.send_keys(text)
 
 
 def clear(self,locator):
      element=self.find_element(locator)
      element.clear()
     
 def is_text_in_element(self,locator,text,timeout=10):   
    '''判断文本在元素里，没定位到元素返回false，定位到返回判断结果布尔值'''
    try:
        result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))
    except TimeoutException:
        print("没有定位到元素"+str(locator))
        return False
    else:
        print("成功定位到元素")
        return result
 def alert_is_present(self,timeout=5):
       '''判断页面是否有alert'''
     
       result=WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())
       if result :
          print(result.text)
          return result
          
       else:
           print("alret 未弹出")

 def accept_alert(self,timeout=5):
     ''' 接受弹框'''
     self.driver.switch_to.alert.accept()
 def dismiss_alert(self,timeout=5):
     '''拒绝弹框'''
     self.driver.switch_to.alert.dismiss()
 def move_to_element(self,locator):
    '''鼠标悬停操作'''
    
    #self.driver.move_to_element(locator)  
    element=self.find_element(locator)
    ActionChains(self.driver).move_to_element(element).perform()
    
 def back(self):
    '''返回上一个窗口''' 
    self.driver.back()
    
 def forward(self):
    self.driver.forward()   
    
    
 def close(self):
    self.driver.close()   
    
 def quit(self):
    self.driver.quit()
    
 def get_title(self):
    '''获取title'''
    return self.dirver.title
 def get_text(self,locator):
    element=self.find_element(locator)
    return element.text

 def get_attribute(self,locator,name):
    ''' 获取属性'''
    element=self.find_element(locator)
    return element.get_attribute(name)

 def js_execute(self,js):
    '''执行js语句'''
    return self.driver.execute_script(js)

 def js_focus_element(self,locator):
    '''聚焦元素'''
    target=self.find_element(locator)
    self.driver.excute_script("arguments[0].scrollIntoView();",target)    
    
 def js_scroll_top(self):
    '''滚动到顶部'''
    js="window.scrollTo(0,0)"
    self.driver.execute_script(js) 
    
 def js_scroll_end(self):
    '''滚动到底部'''
    js="window.scrollTo(0,document.body.scrollHeight)"
    self.driver.execute_script(js)          
 def select_by_index(self,locator,index):
    '''通过索引，index是索引第几个，从0开始'''
    
    element=self.find_element(locator)
    sleep(2)
    Select(element).select_by_index(index)
 def select_by_value(self,locator,value):
    '''通过value属性'''
    element=self.find_element(locator)
    sleep(2)
    Select(element).select_by_value(value) 
 def select_by_text(self,locator,text):
    '''通过text属性'''
    element=self.find_element(locator)
    sleep(2)
    Select(element).select_by_visible_text(text)
    
 def open_new_window(self):
    #页面的跳转
        current_windows = self.driver.current_window_handle
        #self.find_element(element).click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)
    
    
 def  switch_to_frame(self,element):
    ''' 切换到iframe'''
    self.driver.switch_to_frame(self.find_element(element))
    
 def  switch_to_frame_out(self):
    ''' 切换出iframe'''
    self.driver.switch_to_default_content()
    
    
    
    
    
    
    
    
    
    
    