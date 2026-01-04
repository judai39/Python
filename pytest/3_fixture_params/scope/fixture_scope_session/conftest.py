# 对于让所有测试文件都能观察到的装饰器,当然是要声明为conftest.py中单独存放了

import pytest

@pytest.fixture(scope='session')
def function_scope_session():
    print("这是一次会话session,装饰了测试类!")
