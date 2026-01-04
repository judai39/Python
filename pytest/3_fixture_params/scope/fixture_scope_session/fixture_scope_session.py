# 如果需要同时调用多个测试文件,还仅希望装饰器仅被调用一次
# 对于class,生效范围为当前class中的所有类,调用多个文件会把所有单独的类全部调用一次装饰器
# 对于module,和class同理,调用多个测试文件需要创建多个装饰器
# 对于function,创建更多装饰器!!!
# 因此有了session返回,译为会话,在当前调用场景下,仅调用一次装饰器

import pytest

class TestScopeSession:
    def test_scope_session1(self,function_scope_session):
        print("这是会话session中的第一次测试")
    def test_scope_session2(self,function_scope_session):
        print("这是会话session中的第二次测试")

if __name__=="__main__":
    # 会话中的执行顺序由main调用顺序决定
    pytest.main(["-vs","pytest/3_fixture_params/scope/fixture_scope_session/fixture_scope_session_odds.py","pytest/2.2_fixture/fixture_scope_session/fixture_scope_session.py"])