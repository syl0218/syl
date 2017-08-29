'''
Created on 2017年4月13日

@author: syl
'''
#from selenium import webdriver
from time import sleep
from common.Login import login
from common.NewLive import NewaLive
import unittest
from common.mytest import MyTest
import ddt
from common.log import Log   
from common import exceltest
data1=exceltest.ExcelUtil("login.xlsx","Sheet1")
logindata=data1.dict_data()           
log=Log()
@ddt.ddt
class Changetime(MyTest):   

    @ddt.data(*logindata)
    def test_changeItem2(self,data):      
        #元素
        driver=self.driver
        modify=("class name","modify")
        permissionconfig=("link text","权限设置")
        passwordvisit=("css selector","input[value='vCode']")
        valcontent=("name","valContent")
        tipcontent=("name","tipContent")
        live_edit_auth=("class name","live-edit-auth")  
        
       
        #操作
        log.info("------test_changeitem2-----")
        driver.get("http://192.168.133.217") 
        login().userlogin1(driver,data["username"],data["password"])
        sleep(3)
        NewaLive().newalive1(self.driver)
        self.driver.open_new_window()
        driver.click(modify)   
        self.driver.click(permissionconfig)
        self.driver.click(passwordvisit)
        self.driver.send_keys(valcontent, "123")
        self.driver.send_keys(tipcontent,"password")
        self.driver.click(live_edit_auth)
        sleep(3)
if __name__ == "__main__":
    unittest.main()  
        
        
        
        
        
               
                
                