'''
Created on 2017年6月30日

@author: syl
'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.application import MIMEApplication


sender="86476298@qq.com"
_pwd="ocgdqaiqqwqmcbac"
receiver="354680613@qq.com"
msg=MIMEMultipart()
msg["Subject"]="测试一下python邮件"
msg["From"]=sender
msg["To"]=receiver
part=MIMEText("nihao")
att1=MIMEText("E:\python\report\2017-06-26_17-31-01result.html",'html')
att1.add_header('Content-Disposition','attachment',filename='2017-06-26_17-31-01result.html')
msg.attach(att1)


try:
   s=smtplib.SMTP_SSL("smtp.qq.com",465)
   s.login(sender,_pwd)
   s.sendmail(sender,receiver,msg.as_string())
   s.quit()
   print("邮件发送成功")
except smtplib.SMTPException as e:
    print("邮件发送失败")
 