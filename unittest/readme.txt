1、什么是Unittest框架？

    python自带一种单元测试框架

2、为什么使用UnitTest框架？

    >批量执行用例
    >提供丰富的断言知识
    >可以生成报告

3、核心要素

  1).TestCase（测试用例）
  2).TestSuite(测试套件)
  3).TestRunner(测试执行，执行TestUite测试套件的)
  4).TestLoader(批量执行测试用例-搜索指定文件夹内指定字母开头的模块) 【推荐】
  5) Fixture(固定装置(两个固定的函数，一个初始化时使用，一个结束时使用))

接下来会展开 核心要素来认识unittest框架：

首先介绍下unittest的用例规则：

​ 1、测试文件必须导包：import unittest

​ 2、测试类必须继承 unittest.TestCase

​ 3、测试方法必须以 test_开头