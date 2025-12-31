import unittest
from ddt import ddt, data,unpack
 
@ddt  
class TestDemo(unittest.TestCase):
    # 单一参数
    @data('17611110000', '17611112222')
    def test_1(self, phone):
        print('测试一电话号码：', phone)

    # @data传入多个参数,以列表的形式,需要unpack解包
    @data(["admin","12345"])
    @unpack
    def test_2(self,username,password):
        print('测试二账号',username,password)
        
if __name__ == '__main__':
    unittest.main()
else:
    pass