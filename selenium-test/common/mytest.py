'''
Created on 2017年7月17日

@author: syl
'''
import unittest
from common.fengzhuang import syl
from common.log import Log

class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### Start ###############################')
        self.driver =syl("chrome")
       

    def tearDown(self):
        self.driver.quit()
        self.logger.info('###############################  End  ###############################')