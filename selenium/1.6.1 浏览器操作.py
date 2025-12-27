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

# 1.处理alert弹窗对象
# driver.execute_script("alert('这是一个alert弹窗');")
# from selenium.webdriver.common.alert import Alert
# alert=Alert(driver) #获取弹窗对象,这里的弹窗对象是get()所在的网页
# print(alert.text)
# alert.accept()
# driver.quit()

#2.处理confirm弹窗对象
# driver.execute_script("confirm('这是一个confirm弹窗');")
# from selenium.webdriver.common.alert import Alert
# alert=Alert(driver)
# print(alert.text)
# alert.accept()  #alert.dismiss()
# driver.quit()

#3.处理prompt弹窗对象
# driver.execute_script("prompt('这是一个promt弹窗')")
# from selenium.webdriver.common.alert import Alert
# alert=Alert(driver)
# print(alert.text)
# alert.send_keys("用户输入")
# alert.accept()
# driver.quit()