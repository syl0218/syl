'''
Created on 2017年6月27日

@author: syl
'''
import unittest

class test(unittest.TestCase):
    
    @unittest.skip("无条件跳过")
    def test01(self):
        print("01")
        
        
    @unittest.skipIf(True,"123")
    def test02(self):
        print("02")
        
    @unittest.skipUnless(False,"132")
    def test03(self):
        print("03")
        
    @unittest.expectedFailure
    def test04(self):
        print("04")
        self.assertEqual(2,2, msg="xiangdeng")
   
        
if __name__ == "__main__":
   
    unittest.main()       