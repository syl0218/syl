'''
Created on 2017年7月11日

@author: syl
'''
import ddt
import unittest
from exceltest import ExcelUtil ,data,filePath,sheetName
from selenium import webdriver
from time import sleep
testData=data.dict_data()
#print(testData)

@ddt.ddt
class Qlm(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        url="http://192.168.133.217"
        self.driver.get(url)
        self.driver.implicitly_wait(10)
    def login(self,username,psw):
        self.driver.find_element_by_class_name("check_login_start").click()
        sleep(2)
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("password").send_keys(psw)
        
        self.driver.find_element_by_class_name("btn-login-submit").click()
        sleep(5)
    @ddt.data(*testData)   
    def test_login(self,data):
        print("当前测试数据%s"%data)        
        self.login(data['username'],data['password'])
        
    def tearDown(self):
       self.driver.quit()
if __name__ == "__main__":
   unittest.main()      
            