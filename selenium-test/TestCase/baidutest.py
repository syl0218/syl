'''
Created on 2017年7月19日

@author: syl
'''
from time import sleep
from common import mytest
from page import baidupage
import unittest
class baidutest(mytest.MyTest):
    url=('http://www.baidu.com')  
    def test_search(self):
        baidu=baidupage.BaiduIndexPage(self.driver)        
        baidu.into_baidu_page(self.url)
        baidu.input_search_key("selenium")
        baidu.click_search_button()
        sleep(4)
        
        
        
if __name__ == "__main__":
    unittest.main()       