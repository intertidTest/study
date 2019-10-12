#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/9/7 14:57
#@Author: zz
#@File  : logger.py
import logging
from logging.handlers import TimedRotatingFileHandler
import os,sys,time
from config import readconfig
#如果日志目录不存再，则创建一个logs
if not os.path.exists(readconfig.log_dir):os.mkdir(readconfig.log_dir)
class Log():
    def __init__(self):
        #文件的命名
        self.logname=os.path.join(readconfig.log_dir,'test%s.log'%time.strftime('%Y-%m-%d'))#文件名一样发现不会再次创建
        self.logger=logging.getLogger()#创建一个logger对象，它提供了应用程序可以直接使用的接口
        #self.logger.handlers.clear()
        self.logger.setLevel(logging.INFO)
        #日志输出格式
        self.formatter=logging.Formatter('%(asctime)s -[ %(filename)s|%(funcName)s] - %(levelname)s - %(message)s')
    #前面有__表私有，不能被导入
    def __console(self,level,message):
        #fh=TimedRotatingFileHandler(filename=self.logname,when='d',encoding='utf-8')#用于每天写一个日志，不明白作用
        fh=logging.FileHandler(self.logname,encoding='utf-8')#创建一个handler，用于写到本地位置文件，启动一次一个日志
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)#给logger添加handler
        #创建一个StreamHandler，用于控制台输出
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level=='info':
            self.logger.info(message)
        elif level=='debug':
            self.logger.debug(message)
        elif level=='warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)

            #移除handler，避免日志输出重复
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
        #关闭文件
        fh.close()
    def debug(self,message):
        self.__console('debug',message)
    def info(self,message):
        self.__console('info',message)
    def warning(self,message):
        self.__console('warning',message)
    def error(self,message):
        self.__console('error',message)
# if __name__=="__main__":
#     log=Log()
#     log.error('11error')
#     log.error('12error')
#     log.info('11info')
