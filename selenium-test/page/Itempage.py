'''
Created on 2017年7月19日

@author: syl
'''
from page import basepage
class itempage(basepage):
    account_set_li=("class name","account-set-li")      
    description=("name","description")      
    account_home_btn_save=("class name","account-home-btn-save")      
    btn_primary=("class name","btn-primary")
    go_user_page=("class name","go-user-page")
     
   
    
    def click_account_set_li(self):
        self.driver.click(self.account_set_li)
    def clear_descroption(self):
        self.driver.clear(self.description)    
    def input_description(self,des):
        self.driver.send_keys(self.description,des)
    def click_save_btn(self):
        self.driver.click(self.account_home_btn_save)
    def click_btn_primary(self):
        self.driver.click(self.btn_primary)
        