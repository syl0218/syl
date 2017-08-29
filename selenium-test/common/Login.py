'''
Created on 2016年11月29日

@author: syl
'''
from selenium import webdriver
from time import *
from common.fengzhuang import syl
#登陆
class login():
     def userlogin1(self,driver,user,psw):  
         #元素
         loginstart=("class name", "check_login_start")
         loginstart2=("css selector",".check_login_start")
         username=("name","username")
         passwd=("name","password")
         submit=("class name","btn-login-submit")
         a=("class name","username-error")
         b=("class name","password-error")
         #操作         
            
         driver.click(loginstart2)
             
         driver.send_keys(username,user) 
      
         driver.send_keys(passwd,psw)
        
         driver.click(submit)      
         #driver.is_text_in_element(a,"用户名为必填项")   
         #driver.is_text_in_element(b,"密码为必填项")    
     def userlogout(self): 
         logout=("class name","nav-logout")        
         self.driver.click(logout)             
        

         
     