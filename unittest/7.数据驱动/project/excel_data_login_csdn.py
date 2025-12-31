import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack
import openpyxl as openpyxl

# 读取excel中的信息,使用xlrd,openpyxl
def read_excel():
    xlsx=openpyxl.load_workbook("unittest/7.数据驱动/project/account_message.xlsx")
    sheet1=xlsx['Sheet1']
    print(sheet1.max_row)
    print(sheet1.max_column)
    print('=======================================================')
    allList=[]
    for row in range(2,sheet1.max_row+1):
        # 每次都会新建一个rowlist,对的,最后需要把所有
        rowlist=[]
        for column in range(1,sheet1.max_column+1):
            rowlist.append(sheet1.cell(row,column).value)
        allList.append(rowlist)
    return allList

print(read_excel())