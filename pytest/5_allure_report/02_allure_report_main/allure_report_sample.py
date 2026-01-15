import pytest
import allure
import os

@allure.epic("示例项目")
@allure.feature("计算功能")
@allure.story("加法场景")
@allure.title("加法用例 - 正常情况")
@allure.severity(allure.severity_level.CRITICAL)
def test_add():
    with allure.step("步骤1：计算 1 + 1"):
        result = 1 + 1
    with allure.step("步骤2：断言结果等于2"):
        assert result == 2, "加法结果应为2"

if __name__=="__main__":
    pytest.main(["-vs","pytest/5_test_report/02_allure_report_parameters/allure_report_sample.py"
                 ,"--alluredir=pytest/5_test_report/02_allure_report_parameters/allure-results/"])
    # allure的其他带参数的命令都是在命令行中运行的,python如何调用系统的命令行操作?
    #       ---->使用os.systme()
    #  !!!!allure-pytest安装到pip中的不是allure工具,而是适用于pytest的allure工具适配器
    # 因此需要下载allure项目并且配置环境到path
    # 1.创建allure项目报告网页web项目
    # !!!!此处创建的路径中的文件是jsp项目
    os.system("allure generate pytest/5_test_report/02_allure_report_parameters/allure-results -o pytest/5_test_report/02_allure_report_parameters/allure-report --clean")
     # 2.打开项目报告网页web项目
    #  !!!!此处打开路径中的文件是json文件
    # os.system(r"allure open pytest/5_test_report/02_allure_report_parameters/allure-results")
    # 或者可以启动临时服务查看web项目                                        
    os.system("allure serve pytest/5_test_report/02_allure_report_parameters/allure-results")