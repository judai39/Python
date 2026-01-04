import pytest
@pytest.fixture(scope='module')
def function_scope_module():
    print("module级别装饰器,生效范围为py文件的第一个测试方法")

class TestModuleScope():
    def test_01(self,function_scope_module):
        print("test_01测试方法在第一个类中的第一个方法处被调用,会被装饰")
    def test_02(self,function_scope_module):
        print("test_02测试方法在第一个类中的第二个方法处被调用,不会被装饰")

class TestModuleScope2():
    def test_03(self,function_scope_module):
        print("test_03测试方法在第二个类中被调用了,不会被装饰")
    def test_04(self,function_scope_module):
        print("test_03测试方法在第二个类中被调用了,不会被装饰")
if __name__=="__main__":
    pytest.main(['-vs','pytest/3_fixture_params/scope/fixture_scope_module.py'])