import pytest 
def test_01():
    print("这是一个测试函数")

if __name__=="__main__":
    # 注意pytest测试文件的命名必须以test开头且符合py文件的命名格式
    pytest.main(['-v','pytest/1_sample/test_main.py'])
    

# 其他参数
# -v	输出调试信息。如：打印信息	pytest.main([‘-v’,‘testcase/test_one.py’,‘testcase/test_two.py’])
# -s	输出更详细的信息，如：文件名、用例名	pytest.main([‘-vs’,‘testcase/test_one.py’,‘testcase/test_two.py’])
# -n	多线程或分布式运行测试用例	
# -x	只要有一个用例执行失败，就停止执行测试	pytest.main([‘-vsx’,‘testcase/test_one.py’])
# – maxfail	出现N个测试用例失败，就停止测试	pytest.main([‘-vs’,‘-x=2’,‘testcase/test_one.py’]
# –html=report.html	生成测试报告	pytest.main([‘-vs’,‘–html=./report.html’,‘testcase/test_one.py’])
# -m	通过标记表达式执行	
# -k	根据测试用例的部分字符串指定测试用例，可以使用and，or	

# -html参数不可用,使用命令行 pytest --html=report.html ../.py

# 命令行pytest测试参数
# -v	输出调试信息。如：打印信息	pytest -x ./testcase/test_one.py
# -q	输出简单信息。	pyets -q ./testcase/test_one.py
# -s	输出更详细的信息，如：文件名、用例名	pytest -s ./testcase/test_one.py
# -n	多线程或分布式运行测试用例	
# -x	只要有一个用例执行失败，就停止执行测试	pytest -x ./testcase/test_one.py
# – maxfail	出现N个测试用例失败，就停止测试	pytest --maxfail=2 ./testcase/test_one.py
# –html=report.html	生成测试报告	pytest ./testcase/test_one.py --html=./report/report.html