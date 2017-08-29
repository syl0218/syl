'''
Created on 2017年7月19日

@author: syl
'''
from time import sleep
from page import loginpage

class logintest():    
    def test_login(self,user,psw):
        lg=loginpage.Loginpage(self.driver)
        lg.get()
        lg.click_loginstart()
        lg.input_username(user)
        lg.input_password(psw)
        lg.click_submit()
        sleep(2)
        lg.click_go_user_page()    
        