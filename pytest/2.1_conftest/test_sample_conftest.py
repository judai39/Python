import pytest

def test_sample(login_by_request):
    print("测试一下conftest装饰器文件中的loging_by_request装饰器方法")

def test_sample(login_by_yield):
    print("测试一下conftest装饰器文件中的loging_by_yield装饰器方法")

if __name__=="__main__":
    pytest.main(['-vs','test_sample_conftest.py'])