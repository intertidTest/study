#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/10/11 16:03
#@Author: zz
#@File  : run_all.py
import HTMLTestRunner,os,unittest,time
from config import readconfig

if not readconfig.report_path:
    os.mkdir(readconfig.report_path)
rePath=readconfig.report_path
casePath=readconfig.test_path
def add_case():
    discover=unittest.defaultTestLoader.discover(casePath,pattern='test*.py')
    return discover
def run_case(allCase):
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.path.join(rePath, "result_" + now + ".html")
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'信用平台测试结果如下：',description=u'用例执行情况：')
    runner.run(allCase)
    fp.close()


if __name__=="__main__":
    cases=add_case()
    run_case(cases)
