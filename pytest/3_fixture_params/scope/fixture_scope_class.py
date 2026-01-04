# 类级别的修饰器,每个类都会生效,但是在类中仅生效一次(第一次)
import pytest

@pytest.fixture(scope='class')
def function_scope_class():
    print("类级别的修饰器")

class TestClassScope:
    # fixture生效
    def test_001(self,function_scope_class):
        print("用例001,在类中的第一次测试,修饰器将会生效")
    def test_002(self,function_scope_class):
        print("用例002,在类中的第二次测试,修饰器将不会生效")

class TestClassScope2:
    # fixture生效
    def test_003(self,function_scope_class):
        print("用例003,在类中的第一次测试,修饰器将会生效")
    def test_004(self,function_scope_class):
        print("用例002,在类中的第二次测试,修饰器将不会生效")

if __name__=='__main__':
    pytest.main(['-vs','pytest/3_fixture_params/scope/fixture_scope_class.py'])