'''
Created on 2017年7月11日

@author: syl
'''
import ddt
import unittest
testData=[{"username":"123","password":"123"},
          {"username":"1234","password":"1234"}]

@ddt.ddt
class D(unittest.TestCase):
    
    def setUp(self):
        print("start")
       
    def tearDown(self):
        print("end")
    @ddt.data(*testData)
    def test_ddt(self,data):
        print(data)
        
if __name__ == "__main__":
   unittest.main() 