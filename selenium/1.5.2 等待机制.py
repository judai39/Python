#对应菜鸟Selenium教程中的Selenium隐式,显示等待机制
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.baidu.com")

# 固定等待 time.sleep()

# Fluent Wait结合 polling_every 和 ignoring
element=WebDriverWait(driver,timeout=10,poll_frequency=1,ignored_exceptions=[TimeoutException]).until(
    EC.presence_of_element_located((By.ID,"no_such"))
    # ignore的异常如果为NoSuchElementException依然报错TimeoutException,但是如果反过来就没有报错,
    # 说明igonred_exceptions忽略的是until()中异常,如果目标对象一直不出现也会返回一个父级对象
)
