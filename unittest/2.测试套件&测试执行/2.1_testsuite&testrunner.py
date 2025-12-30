# 1、TestSuite（测试套件）：用来组装，打包 ，管理多个TestCase（测试用例）文件的
# 2、TestRunner(测试执行)：用来执行 TestSuite(测试套件的)
import unittest
from testdemo1 import TestDemo1
from testdemo2 import TestDemo2

suite=unittest.TestSuite()

# 将一个类中的所有方法进行添加
# 套件对象.addTest(unittest.makeSuite(测试类名))
suite.addTest(unittest.makeSuite(TestDemo1))
suite.addTest(unittest.makeSuite(TestDemo2))

# 实例化TestRunner
runner=unittest.TextTestRunner()
runner.run(suite)