import pytest

# 将skipif标记赋值给一个变量,使其成为新的可复用的跳过标记
skip_mark=pytest.mark.skipif(condition=2>1,reason="条件成立,跳过该方法")

class TestSkipIf:
    def test_001(self):
        print("正常执行的测试")
    @skip_mark
    def test_002(self):
        print("跳过该方法?")

if __name__=="__main__":
    pytest.main(["-vs","pytest/4_mark/mark_skip/mark_skipif_sample.py"])