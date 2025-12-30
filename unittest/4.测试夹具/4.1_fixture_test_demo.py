# Fixture是一种代码结构，在某些特定情况下，会自动执行。
# def setUp(),每个测试方法执行之前都会执行 （初始化）
# def tearDown(),每个测试方法执行之后都会执行 （释放）

import unittest

class FixtureTestDemo(unittest.TestCase):
    def setUp(self) -> None:
        print("这是初始化测试方法的方法")
        return super().setUp()
    
    def test_case(self):
        print("这是测试方法")

    def tearDown(self) -> None:
        print("这是执行完测试方法后执行的方法")
        return super().tearDown()
    
    # 如果要自定义setUp,tearDown类方法名称,需要打@classmethod标签
    
if __name__=='__main__':
    unittest.main(verbosity=2)