'''
Created on 2017年7月14日

@author: syl
'''
import unittest
import logging 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from Test1.ExcelTest import excel_table_byindex

#create a log
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#日志处理
#创建 并命名 xxx.txt
handler_critical=logging.FileHandler("test.txt",'w')
handler_critical.setLevel(logging.WARNING)
#输入日志信息
handler_info=logging.StreamHandler()
handler_info.setLevel(logging.INFO)
#日志格式
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_critical.setFormatter(formatter)
handler_info.setFormatter(formatter)
#处理信息
logger.addHandler(handler_info)
logger.addHandler(handler_critical)




class Serach(unittest.TestCase):


    def setUp(self):
       logger.info("----start1---")
       self.driver=webdriver.Chrome()
       self.driver.get("http://www.baidu.com")
       logger.info("----start2----")
    def tearDown(self):
        logger.info("----end1---")
        self.driver.save_screenshot("123.png")
        self.driver.quit()
        logger.info("----end2------")


    def test_search(self):
        logger.info("------test------")
        try:
            self.assertIn("百度一下",self.driver.title)
            searchElement=self.driver.find_element_by_id("kw")            
        except AssertionError:
                logger.critical("test",excel_info=True)
                self.fail("test")
        except NoSuchElementException:
                logger.critical("test",excel_info=True)
                self.fail("test")   
        else:
            searchElement.send_keys("123")
            searchElement.send_keys(Keys.RETURN)
            logger.info("-------test2222--------")       
                
                
                    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(exit=False,warnings="ignore")