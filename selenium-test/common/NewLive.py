
#coding=utf-8
from selenium import webdriver
from time import *
from selenium.webdriver.common.keys import Keys
from common.Login import login
from common.NowDate import NowDate
from common.fengzhuang import syl
from time import sleep
import os
#新建直播
class NewaLive():
    def newalive1(self,driver):
         create=("class name","create-live-a")
         title2=("name","title")
         description2=("name","description")
         start_time=("id","date_timepicker_start")
         end_time=("id","date_timepicker_end")
         create_first=("class name","create-live-btn-first")
         tags2=("name","tags")
         background=("class name","live-create-img")
         create_second=("class name","create-live-btn-second")
         finsh=("class name","btn-modal-builded")
         
         driver.click(create)
         sleep(1)
         driver.send_keys(title2,"title")
         sleep(1)
         driver.send_keys(description2,"des")
         sleep(1)
         driver.send_keys(start_time,NowDate().startdate())
         sleep(1)
         driver.send_keys(end_time,NowDate().enddate())
         sleep(1)
         driver.click(create_first)
         sleep(1)
         driver.send_keys(tags2,"tags")
         sleep(1)
         # driver.send_keys(background,'C:\\Users\\Public\\Pictures\\Sample Pictures\\Desert.jpg')
         #sleep(2)
         driver.click(background)
         os.system("E:\\demo1.exe")
         driver.click(create_second)
         sleep(5)
         driver.click(finsh)
         
         
   
        















