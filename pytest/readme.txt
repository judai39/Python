1）模块名（py文件）必须是以test_开头或者_test结尾
2）测试类（class）必须以Test开头，并且不能带init方法，类里的方法必须以test_开头
3）测试用例（函数）必须以test_开头

pytest执行分为三种,命令行执行,main函数执行,main函数复合pytest.ini文件执行

conftest.py的特点
pytest 会默认读取 conftest.py里面的所有 fixture
conftest.py 文件名称是固定的，不能改动
conftest.py 只对同一个 package 下的所有测试用例生效
不同目录可以有自己的 conftest.py，一个项目中可以有多个 conftest.py
测试用例文件中不需要手动 import conftest.py，pytest 会自动查找


不管是main执行方式还是命令执行,都会去读取pytest.ini文件

@pytest.fixture(scope = "function",params=None,autouse=False,ids=None,name=None)
scope不同范围的生效情况:
    function	函数级 每一个函数或方法都会调用
    class	    函数级 模块级 每一个.py文件调用一次
    module	    模块级 每一个.py文件调用一次
    session	    会话级 每次会话只需要运行一次，会话内所有方法及类，模块都共享这个方法


@pytest.fixture()修饰装饰器
@pytest.mark./...修饰测试方法