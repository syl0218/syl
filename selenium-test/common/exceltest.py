'''
Created on 2017年6月28日

@author: syl
'''
import xlrd,os
from config import globalparam

data_path = globalparam.data_path
class ExcelUtil():
    def __init__(self,excelname,sheetName):
        #打开excel
        datapath = os.path.join(data_path, excelname)
        self.data=xlrd.open_workbook(datapath)
        #选择sheet
        self.table=self.data.sheet_by_name(sheetName)
        self.keys=self.table.row_values(0)
        self.rowNum=self.table.nrows
        self.colNum=self.table.ncols
     
    def dict_data(self):
        
        if self.rowNum<=1:
            print("总行数小于等于1")   
        else:
          r=[]
          j=1
          for i in range(self.rowNum-1):
              s={}
              values=self.table.row_values(j)
              for x in range(self.colNum):
                  s[self.keys[x]]=values[x]
              r.append(s)
              j+=1 
          return r
#filePath="login.xlsx"
#sheetName1="Sheet1"

#data1=ExcelUtil(filePath,sheetName1)    
  
    