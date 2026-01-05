# 借由给pytest-pdb.allure添加参数--clean-alluredir,生成临时的测试报告

import pytest

def test_error_method():
    index=1
    print("这是一个有bug的函数方法")
    assert index==2

if __name__=="__main__":
    pytest.main(["pytest/5_test_report/temp_report/temp_allure_report.py"])
    # pdb调试控制台输入q退出即可生成当前的临时测试报告(json格式)