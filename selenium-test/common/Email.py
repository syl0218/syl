'''
Created on 2017年7月17日

@author: syl
'''
import sys  
import os  
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication
curPath = os.path.abspath(os.path.dirname(__file__))  
rootPath = os.path.split(curPath)[0]  
sys.path.append(rootPath)
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
  #发送邮件
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