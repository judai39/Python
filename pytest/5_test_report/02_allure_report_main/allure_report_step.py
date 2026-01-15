import os
import allure
import pytest

@allure.step("步骤二")
def passing_step():
    assert True
    pass


@allure.step("步骤三")
def step_with_nested_steps():
    nested_step()
    assert True


@allure.step("步骤四")
def nested_step():
    nested_step_with_arguments(1, 'abc')
    assert True


@allure.step("步骤五")
def nested_step_with_arguments(arg1, arg2):
    assert True
    pass


@allure.step("步骤一")
def test_with_nested_steps():
    passing_step()
    step_with_nested_steps()
    assert True

if __name__ == '__main__':
    pytest.main(['-s', '-q','pytest/5_test_report/02_allure_report_parameters/allure_report_step.py',
                 '--clean-alluredir','--alluredir=pytest/5_test_report/02_allure_report_parameters/allure-results'])
    os.system(r"allure generate -c -o pytest/5_test_report/02_allure_report_parameters/allure-results pytest/5_test_report/02_allure_report_parameters/allure-report")
    # os.system(r"allure open pytest/5_test_report/02_allure_report_parameters/allure-results")
    os.system(r"allure serve pytest/5_test_report/02_allure_report_parameters/allure-results")