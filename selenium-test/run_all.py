'''
Created on 2017年6月26日

@author: syl
'''


import unittest
import time,os
import HTMLTestRunnerCN
from common.Email import sendmail,new_report
from config import globalparam
#遍历所有的用例
def all_case():
    case_dir="E:\\eclipse\\workplace\\selenium-test\\TestCase"
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir, pattern="Change*.py", top_level_dir=None)
    for test_cases in discover:
        for test_case in test_cases:
            testcase.addTests(test_case)   
    print(testcase)            
    return testcase
            
if __name__ == "__main__":
    
    runner=unittest.TextTestRunner()
    test_report=globalparam.report_path
    
    now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()) 
    filename=os.path.join(test_report,'%s.html'%now)
    fp = open(filename,"wb")
    runner =HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='自动化测试报告',description='测试结果：',tester="syl")
    runner.run(all_case())
    fp.close()
    new_report =new_report(test_report)
    sendmail(new_report)
    