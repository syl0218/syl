'''
Created on 2016年12月27日

@author: syl
'''
import unittest
from selenium import webdriver
from time import *
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from case.fengzhuang import syl
import xlrd
import types
def open_excel(file= 'login.xlsx'):
        try:
                data = xlrd.open_workbook(file)
                return data
        except Exception as e:
                print (str(e))
        #根据索引获取Excel表格中的数据 参数:file：Excel文件路径 colnameindex：表头列名所在行的所以 ，by_index：表的索引
def excel_table_byindex(file= 'login.xlsx',colnameindex=0,by_index=0):
        data = open_excel(file)
        table = data.sheets()[by_index]
        nrows = table.nrows #行数
        colnames = table.row_values(colnameindex) #某一行数据
        list =[]
        for rownum in range(1,nrows):
                row = table.row_values(rownum)
                if row:
                        app = {}
                        for i in range(len(colnames)):
                                app[colnames[i]] = row[i]
                        list.append(app)
        return list
def Login(driver):
        listdata= excel_table_byindex("E:\\login.xlsx")
        
        if (len(listdata) <= 0 ):
                assert 0 ,u"Excel数据异常"
        for i in range(0,len(listdata)):                 
                if isinstance(listdata[i]['username'],float):
                    username=str(int(listdata[i]['username']))
                if isinstance(listdata[i]['password'],float):   
                    password=str(int(listdata[i]['password']))               
                if isinstance(listdata[i]['username'],str):
                   username=listdata[i]['username']
                if isinstance(listdata[i]['password'],str):
                    password=listdata[i]['password']
              
              
                
               #元素
                loginstart=("class name", "check_login_start")
                username1=("name","username")
                passwd=("name","password")
                submit=("class name","btn-login-submit")
                #操作         
                sleep(2)
                driver.click(loginstart)
                sleep(2)  
                driver.send_keys(username1,username)   
                sleep(2)
                driver.send_keys(passwd,password)
                sleep(2)
                driver.click(submit)          
               
              
              
              
              
              
              
              
'''              
                    
if __name__ == "__main__":
    driver=syl()
    driver.get("http://192.168.133.217")
    Login(driver)
'''