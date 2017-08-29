'''
Created on 2016年12月23日

@author: syl
'''
 #coding=utf-8
import sys  
import os  
curPath = os.path.abspath(os.path.dirname(__file__))  
rootPath = os.path.split(curPath)[0]  
sys.path.append(rootPath)  
  
import unittest
import HTMLTestRunner
import time
from case import ChangePassWord
from case import ChangeName
from case import ChangeItem
from case import ChangeTime
from case import Login


suite=unittest.TestSuite()

suite.addTest(unittest.makeSuite(ChangeItem.Changeitem))
suite.addTest(unittest.makeSuite(ChangePassWord.changePassWord)) 
suite.addTest(unittest.makeSuite(ChangeName.changename))
suite.addTest(unittest.makeSuite(ChangeTime.Changetime))

runner=unittest.TextTestRunner()   
 #获取当前时间，这样便于下面的使用。
now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()) 

filename="E:\\python\\report\\"+now+"result.html"
fp = open(filename,"wb")
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report',description='result：')
runner.run(suite)
fp.close()