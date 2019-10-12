#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/9/11 17:20
#@Author: zz
#@File  : driver.py
from selenium import webdriver
import time
from public.comment.logger import Log
log=Log()
def browser():
    try:
        driver = webdriver.Firefox()
        driver.maximize_window()
        return driver
    except Exception as msg:
        log.error("驱动异常{0}".format(msg))
