import pytest

def test_sample1(login_by_request):
    print("测试一下conftest装饰器文件中的loging_by_request装饰器方法")

def test_sample2(login_by_yield):
    print("测试一下conftest装饰器文件中的loging_by_yield装饰器方法")

if __name__=="__main__":
    pytest.main(['-vs','pytest/2_conftest/test_sample_conftest.py'])