# pip install pytest-rerunfailures
import pytest
import random

# 测试失败后重试的两种方式:
# 1.标记特定用例(特定测试方法失败)
flaky=pytest.mark.xfail(2>1,"标注为预期失败")
# rerun失败后立即重试次数,reruns_delay决定重新运行时间
@pytest.mark.flaky(reruns=3,reruns_delay=2)
def test_flaky_method():
    # 有一半的概率测试失败
    assert random.choice([True,False])

if __name__=="__main__":
    pytest.main(['-vs','pytest/4_mark/mark_xfail/mark_rerunfailures_sample.py'])

# 2.命令行参数(全局)
# if __name__=="__main__":
#     pytest.main(['-vs','--reruns=3','--reruns-delay=1','pytest/4_mark/mark_xfail/mark_rerunfailures_sample.py'])

# 重新运行参数:--lf(添加参数后,测试命令会执行两遍,第二遍将会只执行错误的测试方法)
#             --reruns(添加参数后,测试命令只会执行一遍,在发生错误后立即重新执行该测试方法直到上线次数)