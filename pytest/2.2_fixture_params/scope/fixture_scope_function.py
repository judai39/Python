import pytest

# scope='function'(默认值,可以不声明),该包中的所有函数均会生效
@pytest.fixture()
def function_scope_fixture():
    print("函数级的修饰器,生效范围为'每一个函数'")
    return "修饰器返回值1"

@pytest.fixture()
# 将其他装饰器当作参数传入,调用时会传入作为参数构造器的代码块,并且传入本装饰器的代码块
def function_scope_fixture_include(function_scope_fixture):
    print("函数级的修饰器,生效范围为'每一个函数',被其他修饰器调用了")

class TestFunctionScope:
    def test_001(self,function_scope_fixture):
        print("用例001/n")
        print("返回值为:{}".format(function_scope_fixture))
    def test_002(self,function_scope_fixture_include):
        print("用例002/n")
        print("返回值为:{}".format(function_scope_fixture_include))

if __name__=='__main__':
    pytest.main(['-vs','pytest/2.2_fixture_params/scope/fixture_scope_function.py'])