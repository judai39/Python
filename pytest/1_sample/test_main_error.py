import pytest
# pytest框架如何调试代码
# pip install pytest-pdb安装调试插件
# pytest test.py --pdb
# 也可以在pytest.ini文件中配置addopts选项,添加参数--pdb
# pytest test.py --pdb --trace  返回开头,从头开始调试代码
# pytest test.py --pdb --alluredir=pytest/1_sample/tmp/report 生成临时调试结果报告(需要pip install allure-pytest)

def test_error_method():
    index=0
    print("这是带有bug的测试方法")
    assert index==1

if __name__=="__main__":
    pytest.main(['-vs','pytest/1_sample/test_main_error.py'])
# 进入pdb调试界面后,调试命令:
# 命令	    含义
# l 或 list	查看当前行附近的代码
# n 或 next	执行下一行代码
# s 或 step	进入函数内部
# c 或 continue	继续执行直到下一个断点或程序结束
# q 或 quit	退出调试
# p 变量名	打印变量的值
# pp 变量名	更清晰地打印变量（pretty print）