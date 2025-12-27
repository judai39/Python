#对应菜鸟Selenium教程中的Selenium浏览器操作
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.baidu.com")

#driver.execute_script("浏览器操作")  执行script操作
driver.execute_script("window.open('https://www.bilibili.com');")

#4切换窗口与标签页
# window_handles=driver.window_handles    #获取所有页面窗口对象并封装成数组
# driver.switch_to.window(window_handles[0])
# print(driver.title)
# driver.switch_to.window(window_handles[0])
# driver.quit()

#5.处理iframe
iframe=driver.find_element(By.ID,"iframe")