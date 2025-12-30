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


TestSuite与TestLoader区别：
	共同点：都是测试套件
	不同点：实现方式不同
		TestSuite: 要么添加指定的测试类中所有test开头的方法，要么添加指定测试类中指定某个test开头的方法
		TestLoader: 搜索指定目录下指定字母开头的模块文件中以test字母开头的方法并将这些方法添加到测试套件中，最后返回测试套件