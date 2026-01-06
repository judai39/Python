import pytest
# xfail测试成功返回xpass（常用于提示未修复的已知bug）
@pytest.mark.xfail(2>1,reason="标注为预期失败")
def test_001():
    print("----xpass尚未修复bug----")
    assert True

# xfail测试失败返回xfail（常用于提示未实现的功能）
@pytest.mark.xfail(2>1,reason="标注为预期失败")
def test_002():
    print("----xfail尚未实现功能----")
    assert False

if __name__=="__main__":
    pytest.main(["-vs","pytest/4_mark/mark_xfail/mark_xfail_sample.py"])