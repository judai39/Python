import pytest

@pytest.mark.xfail(2>1,reason="标注为预期失败")
def test_001():
    print("----预期失败的测试方法----")

if __name__=="__main__":
    pytest.main(["-vs","pytest/4_mark/mark_xfail/mark_xfail_sample.py"])