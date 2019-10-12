#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/10/11 14:12
#@Author: zz
#@File  : screenshot.py
import sys,os
from config import readconfig
def intert_img(driver,file_name):
    path=readconfig.img_path+'//'+file_name
    return driver.get_screenshot_as_file(path)