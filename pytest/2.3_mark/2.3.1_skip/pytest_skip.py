# 函数调用模块级跳过，相当于break关键字
import pytest
def pytest_skip_in_function():
    n=1
    while True:
        print(f"这是第{n}条用例")
        n+=1
        if n==5:
            pytest.skip(reason="执行到第五条用例退出")

# 在测试函数中使用模块级跳过，跳过整个模块
import sys
if sys.platform.startswith("win"):
    # 声明allow_module_level为true,允许开启模块跳过
    pytest.skip("跳过windows平台的测试",allow_module_level=True)

@pytest.fixture(autouse=True)
def fixture_001():
    print("这里是装饰器")

def test_001():
    print("测试方法001")