

from time import sleep
from common.Login import login
import unittest
from common.mytest import MyTest
import ddt
from common.log import Log   
from common import exceltest
data1=exceltest.ExcelUtil("login.xlsx","Sheet1")
logindata=data1.dict_data()           
log=Log()
@ddt.ddt
class changePassWord(MyTest):   

    @ddt.data(*logindata)      
    def test_changepassword(self,data):           
        #点击账户设置
        #元素
        account_set_li=("class name","account-set-li") 
        reset_pwd_a=("class name","reset-pwd-a")
        oldpassword=("name","oldPassword")  
        password=("name","password")
        repassword=("name","repassword")
        btn_resetpwd_submit=("class name","btn-resetpwd-submit")
        btn_primary=("class name","btn-primary")
        go_user_page=("class name","go-user-page")      
        #操作 
        log.info("------test_changepassword-----")   
        driver=self.driver

        driver.get("http://192.168.133.217") 
        login().userlogin1(driver,data["username"],data["password"])
        sleep(3)
        driver.click(go_user_page)           
        driver.open_new_window()    
        driver.click(account_set_li)
        driver.click(reset_pwd_a)
        driver.send_keys(oldpassword,"1234567")
        driver.send_keys(password,"1234567")
        driver.send_keys(repassword,"1234567")
        driver.click(btn_resetpwd_submit)
        sleep(2)
        driver.click(btn_primary)                    
if __name__ == "__main__":
    unittest.main()



