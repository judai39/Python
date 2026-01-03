import pytest

def test_session_odds3(function_scope_session):
    print("这是会话中session的第三次测试")

class TestScopeSessionOdds:
    def test_session_odds4(function_scope_session):
        print("这是会话中session的第四次测试")