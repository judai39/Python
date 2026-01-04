# 在这里书写Fixture装饰器,实现对pytest中的测试文件的setUp,tearDown函数装饰,可以分离冗余代码块实现复用

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# fixture修饰器两种构造方式:
# 1.使用yield构造(修饰器函数不能有返回值)
@pytest.fixture()
def login_by_yield():
    print("调用fixture装饰器方法中yield之前的代码块")
    # 生成器,调用next()才会执行yield之后的代码,yield之前对应setUp,之后对应tearDown
    # yield修饰后的装饰器方法不能有返回值(底层将该方法分为两个方法,如果有返回值,前面的函数由于缺少return部分,会报错))
    yield
    print("调用完毕,执行yield之后的代码块")

# 2.使用request关键构造(修饰器函数可以有返回值)
@pytest.fixture()
def login_by_request(request):
    driver=webdriver.Chrome(service=Service('C:/Users/judai/.chromedriver/chromedriver143/chromedriver.exe'))
    # 自定义tearDown部分为一个单独的函数
    def custom_fixture_teardown():
        tear_down_odds="我是tearDown中的参数"
        print("我是teardown函数部分")
        driver.quit()
        return tear_down_odds
    # 将自定义的tearDown函数注册到request参数中
    request.addfinalizer(custom_fixture_teardown)
    # 继续书写setUp部分的函数,由于不需要拆分代码块,可以有返回值
    print("我是setUp函数部分")
    set_up_odds="我是setUp中的参数"
    return set_up_odds