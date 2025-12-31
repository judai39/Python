import unittest
version=20

class TestDemo(unittest.TestCase):

    @unittest.skip('skip修饰,直接跳过')
    def test_method1(self):
        print("测试用例1-1")

    @unittest.skipIf(version>19,'skipIf自定义跳过条件')
    def test_method2(self):
        print("测试用例1-2")

if __name__=='__main':
    unittest.main(verbosity=2)