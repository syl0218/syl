'''
Created on 2016年12月27日

@author: syl
'''

from time import sleep
from common.Login import login
import unittest
from common.log import Log
from common.mytest import MyTest
import ddt
from common import exceltest
data1=exceltest.ExcelUtil("login.xlsx","Sheet1")
logindata=data1.dict_data()
log=Log()
@ddt.ddt
class changename(MyTest):  
    @ddt.data(*logindata)
    def test_changename(self,data):
        u"改变名字"     
        # 元素
        account_set_li=("class name","account-set-li")
        modify_account_set_btn=("class name","modify-account-set-btn")
        name=("name","name")
        account_home_btn_save=("class name","account-home-btn-save")      
        btn_primary=("class name","btn-primary")
        go_user_page=("class name","go-user-page")
        #操作
        log.info("------test_changname-----")
        driver=self.driver      
        driver.get("http://192.168.133.217")   
        login().userlogin1(driver,data["username"],data["password"])
        sleep(3)
        driver.click(go_user_page)           
        driver.open_new_window()
        driver.click(account_set_li)
        driver.click(modify_account_set_btn)
        driver.clear(name)
        driver.send_keys(name, "骨头测试环境222")
        driver.click(account_home_btn_save)
        sleep(3)
        driver.click(btn_primary)                 
if __name__ == "__main__":
   
    unittest.main()