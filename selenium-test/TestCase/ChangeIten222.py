'''
Created on 2017年7月19日

@author: syl
'''
from time import sleep
from common import mytest
from page import Itempage
import unittest
from common.testlogin import logintest
import ddt
from common import exceltest
data1=exceltest.ExcelUtil("login.xlsx","Sheet1")
logindata=data1.dict_data()
@ddt.ddt
class changeitem222(mytest.MyTest):
    @ddt.data(*logindata)
    def test_item222(self,data):
        #登陆      
        logintest.test_login(self,data["username"],data["password"])       
        #跳转
        self.driver.open_new_window()
        #实例化
        item=Itempage.itempage(self.driver) 
        #操作      
        item.click_account_set_li()     
        item.clear_descroption()    
        item.input_description("")
        item.click_save_btn()
        sleep(3)
        item.click_btn_primary()
if __name__ == "__main__":
    unittest.main()  