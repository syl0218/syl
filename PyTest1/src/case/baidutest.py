'''
Created on 2017年7月13日

@author: syl
'''
from fengzhuang import syl
from time import sleep
import unittest
from log.log import Log
log=Log()
class baidutest(unittest.TestCase):
    def test_baidu(self):
      shezhi=("link text","设置")
      sousuo=("link text","搜索设置")
      s=("id","nr")
      js='document.getElementsByClassName("prefpanelgo")[0].click()'
      log.info("开始")
      self.driver=syl("chrome")   
      log.info("打开百度")  
      self.driver.get("http://www.baidu.com")
      self.driver.move_to_element(shezhi)
      self.driver.click(sousuo)
      self.driver.select_by_text(s,"每页显示50条")     
      self.driver.js_execute(js)
      self.driver.alert_is_present()
      sleep(2)
      self.driver.accept_alert()
      sleep(1)
      self.driver.quit()
      log.info("结束")
if __name__ == "__main__":
    unittest.main()   
              
      