'''
Created on 2017年7月17日

@author: syl
'''
import logging 
import time
import os
from config import globalparam
log_path=globalparam.log_path
class Log():
    def __init__(self):
       #文件的命名
       self.logname=os.path.join(log_path,'%s.log'%time.strftime("%Y-%m-%d"))
       self.logger=logging.getLogger()
       self.logger.setLevel(logging.DEBUG)
       #日志格式
       self.formatter=logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    def __cosole(self,level,message):
           #创建一个FlieHandle,用于写到本地
        fh=logging.FileHandler(self.logname,'a',encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        #创建一个streamHandler，用于输入到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)        
        if level=="info":
            self.logger.info(message)
        elif level=='debug':
            self.logger.debug(message)
        elif level=='warning':
            self.logger.warning(message)
        elif level=='error':
            self.logger.error(message)
        #这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()
    def debug(self,message):
        self.__cosole("debug", message)
        
    def info(self,message):
        self.__cosole("info", message)
        
    def warning(self,message):
        self.__cosole("warning", message)   
        
    def error(self,message):
        self.__cosole("error", message)   
        

        
        
        
        
                