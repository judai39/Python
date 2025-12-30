import unittest
import unittest.test
class TestDemo2(unittest.TestCase):
    # 该方法不会被suite套件识别,因为开头没有test
    def standar_test_def(self):
        print("这是测试demo2中的测试方法")