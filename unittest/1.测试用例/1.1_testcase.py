# 示例代码

import unittest

import unittest.test

# 自定义测试类，需要继承unittest中的TestCase
class TestDemo(unittest.TestCase):
    def test_method1(self):
        print("测试方法1")
    def test_method2(self):
        print("测试方法2")

if __name__=='__main__':
    unittest.main(verbosity=2)

# verbosity参数：
# 0 (静默模式): 你只能获得总的测试用例数和总的结果 比如 总共10个 失败2 成功8
# 1 (默认模式): 非常类似静默模式 只是在每个成功的用例前面有个“.” 每个失败的用例前面有个 “F”
# 2 (详细模式):测试结果会显示每个测试用例的所有相关的信息