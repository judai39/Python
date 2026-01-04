# pytest.mark.parametrize(参数一,[...])允许把参数直接传递给测试方法
# 与fixture(params=,ids=)有什么区别?
# ----fixture.params是将参数交给装饰器,由装饰器批量分发给测试方法,
#     而parametrize是由框架直接分发参数给测试方法
import pytest

# 1.单个参数传值
@pytest.mark.parametrize("test_input,expected",[("3+5",8),("2+4",6)])
def test_mark_parametrize(test_input,expected):
    print(f"pytest框架直接分发给测试方法的数据{test_input},期望结果为{expected}")
    assert eval(test_input)==expected

# 2.多个参数传值(符合笛卡尔积)
data_1=[1,2,3]
data_2=['x','y']
@pytest.mark.parametrize('a',data_1)
@pytest.mark.parametrize('b',data_2)
def test_mark_parametrize(a,b):
    # 产生的结果为[{1,2,3},{x,y}]=[(1,x),(1,y),(2,x),(2,y),(3,x),(3,y)]
    print(f'笛卡尔积,测试数据为:{a},{b}')
# --为什么要返回这样的结果? --为了对应每个测试用例的所有匹配结果

if __name__=="__main__":
    pytest.main(["-vs","pytest/4_mark/mark_parametrize/mark_parametrize_sample.py"])