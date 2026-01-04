import pytest
@pytest.fixture(name="new_fixture_name")
def old_fixture_name():
    print("这里是装饰器")

def test_001(new_fixture_name):
    print("将装饰器以新的名字传入测试方法,生效")
def test_002(old_fixture_name):
    print("将装饰器以旧的名字传入测试方法,不生效")

if __name__=="__main__":
    pytest.main(['-vs','pytest/3_fixture_params/name/fixture_name_sample.py'])