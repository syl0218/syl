'''
Created on 2017年7月4日

@author: syl
'''
import unittest
from fengzhuang import syl
from loginpage import login_url,loginpage

class Login_test(unittest.TestCase):
    def setUp(self):
        self.driver=syl("chrome")
        self.login=loginpage(self.driver)
        self.login.get(login_url)
        
    def login_case(self,username,psw):
        self.login.click_loginstart()
        self.login.input_username(username)
        self.login.input_passwd(psw)
        self.login.click_submit()
    
    def testlogin(self):
        self.login_case("13777559149", "1234567")
    
    def tearDown(self):
        self.driver.quit()
        
if __name__ =="__main":
    unittest.main()