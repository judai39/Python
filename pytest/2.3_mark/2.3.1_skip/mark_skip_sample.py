import pytest

@pytest.fixture
def fixture_method():
    print("这里是装饰器方法")

def test_case_001():
    print("测试用例001")

@pytest.mark.skip(reason="不执行该用例，还没有写好")
def test_case_002():
    print("测试用例002")

class TestClass:
    def test_class_case_001(self):
        print("类中测试用例001")
    @pytest.mark.skip(reason="不执行该用例，该类功能待完善")
    def test_class_case_002(self):
        print("类中测试方法002")

@pytest.mark.skip(reason="类也可以跳过不执行,但是reason不会被输出到控制台")
class TestSkip:
    def method():
        print("该类为拓展功能，还没开始撰写功能")

if __name__=="__main__":
    pytest.main(['-vs','pytest/2.3_mark/2.3.1_skip/mark_skip_sample.py'])