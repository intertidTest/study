#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/8/31 16:00
#@Author: zz
#@File  : login.py

from config import readconfig
import unittest,time,ddt
from testData.read_excel import readExcel
from public.comment.logger import Log
from public.comment.driver import browser
from public.page_obj.login_page import login_page
from public.comment import screenshot
'''import requests
from urllib.request import urlopen'''

'''res = requests.get(url)
source = res.status_code
print ('nihao',source)
if source==200:
    pass
else:
    log.error("地址不正确")'''
'''log=Log()
url = myconfig.url
dr.get(url)
time.sleep(2)'''
data = readExcel()
dicDatas = data.dic_data()
@ddt.ddt
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dr=browser()
      # assert self.dr.get(url), 'Did not land on %s' % url'''
    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
    def login(self,name,password):

        #login_page.name_clear()
        #login_page.password_clear()
        print(2)
        login=login_page(self.dr)
        login.open()
        time.sleep(1)
        login.name_clear()
        login.password_clear()
        login.loginName(name)
        #login_name = (By.NAME, "name")
        #login.find_element(login_name)
        login.login_pw(password)
        login.button_click()
        time.sleep(2)
        #login.login(name,password)
        '''open()
        time.sleep(1)
        login_page.loginName(name)
        login_page.login_pw(password)
        login_page.button_click()'''
    @ddt.data(*dicDatas)
    def test_login(self, dicData ):
        print(3)
        log=Log()
        #i=0
        #j=len(dicData)
        print(dicData)
        log.info("当前执行测试用例ID-> {0} ; 测试点-> {1}".format(dicData['caseId'], dicData['caseName']))
        self.login(dicData['user'], dicData['pwd'])
        po = login_page(self.dr)
        #result=po.loginSuccess()
        if dicData['caseName'] == 'name_empty':
            log.info("检查点->{0}".format(po.nameError()))
            self.assertEqual(po.nameError(), dicData['except1'])
            screenshot.intert_img(self.dr,dicData['caseName']+'.jpg')
        elif dicData['caseName'] in ('name_error', 'pwd_error'):
            log.info("检查点->{0}".format(po.passwordError()))
            self.assertEqual(po.passwordError(), dicData['except1'])
            screenshot.intert_img(self.dr, dicData['caseName'] + '.jpg')
            po.errorClick()
        elif dicData['caseName'] == 'pwd_empty':
            log.info("检查点->{0}".format(po.passwordEmpty()))
            self.assertEqual(po.passwordEmpty(), dicData['except1'])
            screenshot.intert_img(self.dr, dicData['caseName'] + '.jpg')
        elif dicData['caseName'] == 'name_pwd_empty':
            log.info("检查点1->{0},检查点2->{1}".format(po.nameError(), po.passwordEmpty()))
            self.assertEqual(po.nameError(), dicData['except1'])
            self.assertEqual(po.passwordEmpty(), dicData['except2'])
            screenshot. intert_img(self.dr, dicData['caseName'] + '.jpg')
        else:
            log.info("检查点->{0}".format(po.loginSuccess()))
            self.assertEqual(po.loginSuccess(),dicData['except1'])
            screenshot.intert_img(self.dr, dicData['caseName'] + '.jpg')
if __name__=='main':
    unittest.main()