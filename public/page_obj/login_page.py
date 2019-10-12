#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/9/20 16:26
#@Author: zz
#@File  : login_page.py
from public.page_obj.base import BasePage
from selenium.webdriver.common.by import By
import time
class login_page(BasePage):
    login_name=(By.NAME,"name")
    login_password=(By.NAME,"password")
    login_button=(By.XPATH,'//button')
    name_error=(By.XPATH,'//form/div[1]/div/span')
    password_empty=(By.XPATH,'//form/div[2]/div/span')
    login_success=(By.XPATH,'//login-info/span')
    password_error=(By.XPATH,"//div[@class='x-dialog-body']/div[1]")
    error_click=(By.XPATH,"//div[@class='x-dialog-tools']/span")
    def name_clear(self):
        self.find_element(*self.login_name).clear()

    def password_clear(self):
        self.find_element(*self.login_password).clear()

    def loginName(self,username):

        print(11)

        self.find_element(*self.login_name).send_keys(username)

    '''
    def login(self,name,password):
        # login_page.name_clear()
        # login_page.password_clear()
        print(21)
        self.open()
        print(22)
        time.sleep(2)
        self.loginName(name)
        self.login_pw(password)
        self.button_click()
       '''
    def login_pw(self,passwaord):
        self.find_element(*self.login_password).send_keys(passwaord)
    def button_click(self):
        self.find_element(*self.login_button).click()
    def nameError(self):
        return self.find_element(*self.name_error).text
    def passwordEmpty(self):
        return self.find_element(*self.password_empty).text
    def passwordError(self):
       return self.find_element(*self.password_error).text
    def errorClick(self):
        self.find_element(*self.error_click).click()
    def loginSuccess(self):
        return self.find_element(*self.login_success).text