'''
Created on 2017年7月19日

@author: syl
'''
from page import basepage
class BaiduIndexPage(basepage):
     
     kw=("id","kw")
     su=("id","su")
          
     def into_baidu_page(self,url):
        """打开百度首页"""
        self.driver.get(url)
     def input_search_key(self,values):
        """输入搜索关键词"""
        self.driver.send_keys(self.kw,values)
     def click_search_button(self):
        """点击搜索按钮"""
        self.driver.click(self.su)
