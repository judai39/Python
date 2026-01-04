import pytest

# autouse参数(默认false)设置为true,可被观察到的所有测试方法都会自动调用该装饰器

@pytest.fixture(autouse='true')
def autouse_fixture():
    print("我是autouse修饰的装饰器,我会被自动调用,无需传入参数")

class TestAutouseFixture:
    def test_autouse_fixture1(self):
        print("测试方法001")
    def test_autouse_fixture2(self):
        print("测试方法002")

if __name__=="__main__":
    pytest.main(["-vs","pytest/3_fixture_params/autouse/fixture_autouse_sample.py"])