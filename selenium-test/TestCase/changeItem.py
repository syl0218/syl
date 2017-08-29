'''
Created on 2016年12月9日

@author: syl
'''
#coding=utf-8
from time import sleep
from common.Login import login
import unittest
from common.log import Log
import ddt
from common.mytest import MyTest
from common import exceltest
data1=exceltest.ExcelUtil("login.xlsx","Sheet1")
logindata=data1.dict_data()
log=Log()
@ddt.ddt
class Changeitem(MyTest):
    @ddt.data(*logindata)
    def test_changeitem(self,data):                 
        #点击账户设置
        #元素              
        account_set_li=("class name","account-set-li")      
        description=("name","description")      
        account_home_btn_save=("class name","account-home-btn-save")      
        btn_primary=("class name","btn-primary")
        go_user_page=("class name","go-user-page")
        #操作
        log.info("------test_changeitem-----")
        driver=self.driver
        driver.get("http://192.168.133.217") 
        login().userlogin1(driver,data["username"],data["password"])    
        sleep(3)
        driver.click(go_user_page)           
        driver.open_new_window()
        driver.click(account_set_li)
        sleep(3)
        driver.clear(description)
        driver.send_keys(description, "sffgsfg")
        driver.click(account_home_btn_save)
        sleep(2)
        driver.click(btn_primary)               
if __name__ == "__main__":
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        