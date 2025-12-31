import unittest
import json
from ddt import ddt,data,unpack

# 1.解析数据文件中的json类型
def read_json():
    with open('unittest/7.数据驱动/data/user_message.json',encoding='utf-8')as f:
        list_json=json.load(f)
        return list_json
    
# 2.解析数据文件中的txt类型
def read_txt():
    list_txt=[]
    with open('unittest/7.数据驱动/data/user_message.txt',encoding='utf-8')as f:
        for line in f.readlines():
            # strip()去除字符串,split()分割字符串
            list_txt.append(line.strip("/n").split(","))
    return list_txt
    
# 3.解析数据文件中的csv类型
import csv
def read_csv():
    list_csv=[]
    with open("unittest/7.数据驱动/data/user_message.csv",encoding="utf-8")as f:
        file_output=csv.reader(f)
        for r in file_output:
            list_csv.append(r)
    return list_csv
@ddt
class TestDataDemo(unittest.TestCase):
    # @data 里面的 * 含义是实现每个json对象单个传入方法执行，不然会吧json文件里面所用数据全部传入 
	# > * 是元祖；
	# > ** 是字典；
    @data(*read_json())
    @unpack
    def test_json_method(self,username,password):
        print("读取json数据测试:",username,password)

    @data(*read_txt())    
    @unpack
    def test_txt_method(self,username,password):
        print("读取txt数据测试:",username,password)
    
    @data(*read_csv())
    @unpack
    def test_csv_method(self,name,company,phone):
        print("读取csv数据测试:",name,company,phone)


if __name__=='__main__':
    unittest.main(verbosity=2)
else:
    pass