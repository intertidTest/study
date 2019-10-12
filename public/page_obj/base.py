#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/9/17 15:54
#@Author: zz
#@File  : base.py
import os,sys
from public.comment.logger import Log
from config.readconfig import myconfig
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
login_url=myconfig.url
log=Log()
class BasePage:
    def __init__(self,dr,url=login_url):
        self.dr=dr
        self.url=url
    def open(self):
        print(1)
        self.dr.get(self.url)
    def find_element(self,*loc):
        try:
            print(111)
            WebDriverWait(self.dr, 10).until(EC.visibility_of_element_located(loc))
            print(loc)
            return  self.dr.find_element(*loc)
        except:
            print(1111)
            log.error("{0}页面中未能找到{1}元素".format(self,*loc))
    def by_id(self,id_):
        return self.dr.find_element_by_id(id_)
    def by_name(self,name):
        return self.dr.find_element_by_name(name)
    def by_xpath(self,xpath):
        return self.dr.find_element_by_xpath(xpath)
    def by_css(self,css):
        return self.dr.find_element_by_css_selector(css)
    def get_title(self):
        return self.dr.title
    def get_text(self,xpath):
        return self.dr.find_element_by_xpath(xpath).text
    #执行JavaScript脚本
    def js(self,script):
        self.dr.execute_script(script)


