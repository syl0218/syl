'''
Created on 2016年12月9日

@author: syl
'''
import time
import datetime
class NowDate():
    
    def startdate(self):
       starttime= time.strftime('%Y-%m-%d %T',time.localtime(time.time()+5*60))
       return starttime
     
     
    def enddate(self):
        endtime=time.strftime('%Y-%m-%d %T',time.localtime(time.time()+3*60*60))
        return endtime
           
    def changestartdate(self):
       changestarttime= time.strftime('%Y-%m-%d %T',time.localtime(time.time()+30*60))
       return changestarttime 
     
    def changeenddate(self):
        changeendtime=time.strftime('%Y-%m-%d %T',time.localtime(time.time()+5*60*60))
        return changeendtime       