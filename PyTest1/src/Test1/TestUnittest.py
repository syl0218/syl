'''
Created on 2017年6月26日

@author: syl
'''
#添加零时路径
import sys  
import os  
curPath = os.path.abspath(os.path.dirname(__file__))  
rootPath = os.path.split(curPath)[0]  
sys.path.append(rootPath)

import unittest
import time,os
import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication

#发送邮件
def  sendmail(newfile):   
#发件人   密码    收件人    
  sender="86476298@qq.com"
  _pwd="ocgdqaiqqwqmcbac"
  receiver="1263703184@qq.com"
#读取报告的正文 
  f=open(newfile,'rb')
  mail_body=f.read()
  f.close()  
#配置html附件
  msg=MIMEMultipart()
  text=MIMEText(mail_body,'html','utf-8')
  text['Subject']=Header('自动化测试报告','utf-8')  
  msg.attach(text)  
  msg['Subject'] = Header('自动化测试报告', 'utf-8')
  msg_file = MIMEText(mail_body, 'html', 'utf-8')
  msg_file['Content-Type'] = 'application/octet-stream'
  msg_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
  msg.attach(msg_file)  
  #发送附件
  try:
   s=smtplib.SMTP_SSL("smtp.qq.com",465)
   s.login(sender,_pwd)
   s.sendmail(sender,receiver,msg.as_string())
   s.quit()
   print("邮件发送成功")
  except smtplib.SMTPException as e:
    print("邮件发送失败") 
#查找最新的测试报告   
def new_report(testreport):        
    dirs = os.listdir(testreport)
    dirs.sort()
    newreportname = dirs[-1]
    print('The new report name: {0}'.format(newreportname))
    file_new = os.path.join(testreport, newreportname)
    return file_new   
#遍历所有的用例
def all_case():
    case_dir="E:\\eclipse\\workplace\\PyTest1\\src\\case"
    testcase=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(case_dir, pattern="Change*.py", top_level_dir=None)
    for test_cases in discover:
        for test_case in test_cases:
            testcase.addTests(test_case)            
    
    return testcase
            
if __name__ == "__main__":
    runner=unittest.TextTestRunner()
    test_report="E:\\python\\report\\"
    now = time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime()) 
  
    filename=test_report+now+"result.html"
    fp = open(filename,"wb")
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report',description='result：')
    runner.run(all_case())
    fp.close()
    #new_report = new_report(test_report)
    #sendmail(new_report)
    