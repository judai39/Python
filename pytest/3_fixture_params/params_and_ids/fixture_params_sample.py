# 如果希望装饰器可以存储一些能够复用的数据,可以使用params参数

import pytest

@pytest.fixture(params=[1,2,3],ids=["param1","param2","param3"])
def params_fixture(request):
    return request.param

class TestParamsFixture:
    def test_params_fixture(self,params_fixture):
        print(f"score_params:{params_fixture}")

if __name__=='__main__':
    pytest.main(["-vs","pytest/3_fixture_params/params_and_ids/fixture_params_sample.py"])