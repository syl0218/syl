'''
Created on 2017年7月14日

@author: syl
'''
#导入日志模块
import logging

#创建要记录的日志级别的记录器
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#创建日志处理程序
handle_warn=logging.FileHandler("warning_log.text")
handle_warn.setLevel(logging.WARNING)
#日志处理程序创建事物
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handle_warn.setFormatter(formatter)
#将日志处理程序记录到记录器

logger.addHandler(handle_warn)




