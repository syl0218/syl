'''
Created on 2017年7月19日

@author: syl
'''
from page import basepage
class Loginpage(basepage):
    
    loginstart_loc=("class name", "check_login_start")
    username_loc=("name","username")
    passwd_oc=("name","password")
    submit_loc=("class name","btn-login-submit")
    go_user_page=("class name","go-user-page")
    
    
   
    def get(self):
        self.driver.get("http://192.168.133.217")
    def  click_loginstart(self):
        self.driver.click(self.loginstart_loc)
    def input_username(self,user):
        self.driver.send_keys(self.username_loc,user)
    def input_password(self,psw):  
        self.driver.send_keys(self.passwd_oc,psw)
    def click_submit(self):
        self.driver.click(self.submit_loc)       
    def click_go_user_page(self):
        self.driver.click(self.go_user_page)
        