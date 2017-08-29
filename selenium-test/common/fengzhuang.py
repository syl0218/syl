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
import time
from common.log import Log
from turtledemo.clock import hand
log = Log()
success = "SUCCESS   "
fail = "FAIL   "


class syl(object):
    
 
 def __init__(self,browser):
    t1 = time.time()
    '''启动浏览器'''
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
       driver=webdriver.Firefox()
    try:
        self.driver=driver
        self.my_print("{0} Start a new browser: {1}".format(success,browser))
    except Exception :
        self.my_print("Not found this browser,You can enter 'firefox', 'chrome'")    
    self.driver.implicitly_wait(10)
    
    self.driver.maximize_window()
    self.my_print("{0} Set browser window maximized".format(success))
    
 def get(self,url):
     t1 = time.time()
     try:  
        
        self.driver.get(url)
        self.my_print("{0} open  {1}".format(success,url))
     except Exception:
        self.my_print("{0} Unable to load {1}".format(fail, url))  
        raise 
    
    
 def set_window(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        """
        t1 = time.time()
        self.driver.set_window_size(wide, high)
        self.my_print("{0} Set browser window wide: {1},high: {2},".format(success,
            wide,high))
        
 def my_print(self,msg):
        log.info(msg)
 def find_element(self,locator,timeout=10):
    '''定位元素，'''
    try:
      element=WebDriverWait(self.driver,timeout,5).until(EC.presence_of_element_located(locator))
      
    except NoSuchElementException:
        self.my_print("{0} unable to find element <{1}>".format(fail,locator))
    else :
        return element
        self.my_print("{0}  find element <{1}>".format(success,locator))
 def find_elements(self,locator,timeout=10):
    '''定位一组元素，参数locator是元祖类型'''
    elements=WebDriverWait(self.driver,timeout,5).until(EC.presence_of_all_elements_located(locator))
    return elements
 def click(self,locator):
    '''点击操作'''
    t1 = time.time()
    try: 
      element=self.find_element(locator)
      element.click()
      self.my_print("{0} Click element:<{1}>".format(success,locator))
    except Exception:
      self.my_print("{0} Unable to click element:<{1}> ".format(fail,locator))
      raise  
    
    
 def right_click(self, element):
    '''鼠标右击''' 
    t1 = time.time()
    try:
        ActionChains(self.driver).context_click(self.find_element(element)).perform()  
        self.my_print("{0} Right click element: <{1}>".format(success,element))
    except Exception:
        self.my_print("{0} Unable to right click element: <{1}>".format(fail, element))
        raise
    
 def double_click(self, element):
    '''鼠标双击''' 
    t1 = time.time()
    try:
        ActionChains(self.driver).double_click(self.find_element(element)).perform() 
        self.my_print("{0} double click element: <{1}>".format(success,element))
    except Exception:
        self.my_print("{0} Unable to double click element: <{1}>, ".format(fail, element))
        raise     
 def send_keys(self,locator,text):
    '''  发送文本输入 '''  
    t1 = time.time()
    try:
      element=self.find_element(locator)  
      element.send_keys(text)
      self.my_print("{0} send_keys element: <{1}> text:{2}".format(success,
                locator,text))
    except Exception:
            self.my_print("{0} Unable to send_keys element:<{1}> text:{2} ".format(fail,
                locator,text))
            raise
 def clear(self,locator):
    try:
      element=self.find_element(locator)
      element.clear()
      self.my_print("{0} Clear element: <{1}>".format(success,locator))
    except Exception:
      self.my_print("{0} unable to Clear  element: <{1}>".format(fail,locator))  
 def is_text_in_element(self,locator,text,timeout=10):   
    '''判断文本在元素里，没定位到元素返回false，定位到返回判断结果布尔值'''
    try:
        result=WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))
    except TimeoutException:
        self.my_print("{0}unable to find element<{1}>".format(fail,str(locator)))
        return False
    else:
        self.my_print("{0} find element<{1}>".format(success,str(locator)))
        return result
 def alert_is_present(self,timeout=5):
       '''判断页面是否有alert'''
     
       result=WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())
       if result :
          print(result.text)
          return result
          
       else:
           self.my_print("alret 未弹出")

 def accept_alert(self,timeout=5):
     ''' 接受弹框'''
     self.driver.switch_to.alert.accept()
     self.my_print("接受弹框")
 def dismiss_alert(self,timeout=5):
     '''拒绝弹框'''
     self.driver.switch_to.alert.dismiss()
     self.my_print("拒绝弹框")
 def move_to_element(self,locator):
    '''鼠标悬停操作'''
    
    #self.driver.move_to_element(locator)  
    element=self.find_element(locator)
    ActionChains(self.driver).move_to_element(element).perform()
    self.my_print("鼠标悬停")
 def back(self):
    '''返回上一个窗口''' 
    self.driver.back()
    
 def forward(self):
    self.driver.forward()   
    
    
 def close(self):
    self.driver.close()   
    
 def quit(self):
    self.driver.quit()
    self.my_print("{0} driver quit".format(success))
    
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
    t1 = time.time()
    try:
        self.driver.execute_script(js)
        self.my_print("{0} Execute javascript scripts: {1}".format(success,js))
    except Exception:
        self.my_print("{0} Unable to execute javascript scripts: {1}".format(fail,
        js))
        raise

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
    time.sleep(2)
    Select(element).select_by_index(index)
 def select_by_value(self,locator,value):
    '''通过value属性'''
    element=self.find_element(locator)
    time.sleep(2)
    Select(element).select_by_value(value) 
 def select_by_text(self,locator,text):
    '''通过text属性'''
    element=self.find_element(locator)
    time.sleep(2)
    Select(element).select_by_visible_text(text)
    
 def open_new_window(self):
    #页面的跳转
    try:
        current_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != current_windows:
                self.driver.switch_to.window(handle)
                self.my_print("{0}open_new_window <{1}>".format(success,handle.title()))
    except Exception:
                self.my_print("{0}open_new_window <{1}>".format(fail,handle.title()))
 def  switch_to_frame(self,element):
    ''' 切换到iframe'''
    self.driver.switch_to_frame(self.find_element(element))
    
 def  switch_to_frame_out(self):
    ''' 切换出iframe'''
    self.driver.switch_to_default_content()
    
 
    
    
    
    
    