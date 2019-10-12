#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/10/9 15:02
#@Author: zz
#@File  : read_excel.py
import xlrd
from config import readconfig
from public.comment.logger import Log
try:
    path=readconfig.test_data_load+'\\'+readconfig.myconfig.dicDatas
    print(path)
except Exception as msg:
    Log.error("文件不存在{0}".format(msg))
class readExcel():
    def __init__(self,excelPath=path,sheetName="Sheet1"):
        self.excel_Path=excelPath
        self.data=xlrd.open_workbook(self.excel_Path)
        self.table=self.data.sheet_by_name(sheetName)
        self.keys=self.table.row_values(0)#获取第一行为key值
        print(self.keys)
        self.rowNum=self.table.nrows   #总行数
        self.colNum=self.table.ncols   #总列数
    def dic_data(self):
        if self.rowNum<=1:
            print("总行数小于1")
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
if __name__=="__main__":
    #path="D://Python//study//testData//testData.xlsx"
    #data=readExcel(path)
    a=readExcel()
    aa=a.dic_data()
    print()
    print(aa[0]['caseId'])
    print(len(aa))
