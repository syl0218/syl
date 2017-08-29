'''
Created on 2017年7月18日

@author: syl
'''
from fengzhuang import syl
login_url="http://192.168133.217"

class loginpage(syl):
    loginstart=("class name", "check_login_start")
    username=("name","username")
    passwd=("name","password")
    submit=("class name","btn-login-submit")
         
    def click_loginstart(self):
        self.click(self.loginstart)
    def input_username(self,user):
        self.send_keys(self.username, user)
    def input_passwd(self,psw):
        self.send_keys(self.passwd, psw)
    def click_submit(self):
        self.click(self.submit)
        
    def login3(self,user,psw):
        self.click_loginstart()
        self.input_username(user)
        self.input_passwd(psw) 
        self.click_submit()       
        