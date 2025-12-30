# 1. suite = unittest.TestLoader().discover("指定搜索的目录文件","指定字母开头模块文件")
# 2. suite = unittest.defaultTestLoader.discover("指定搜索的目录文件","指定字母开头模块文件") 【推荐】
# 注意：如果使用写法1，TestLoader()必须有括号。

import unittest

# unittest.defaultTestLoader.discover('用例所在的路径', '用例的代码文件名')
# 测试路径：相对路径
# 测试文件名：可以使用 * 通配符，可以重复使用
suite=unittest.defaultTestLoader.discover('./unittest/3.测试加载/Case','Case*.py')
runner=unittest.TextTestRunner()
runner.run(suite)#依旧只会执行开头为test的方法(Test开头也不会执行)