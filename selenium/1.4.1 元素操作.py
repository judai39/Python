#对应菜鸟Selenium教程中的Selenium元素操作
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.bilibili.com")
input_search=driver.find_element(By.XPATH,"//input[@class='nav-search-input']")

input_search.send_keys("selenium教程")


input_search.clear()    #元素被 遮挡 或未处于可编辑状态会失效
#使用send_keys(Keys.keyname)模拟ctrl+a delete键盘输入删除内容
from selenium.webdriver.common.keys import Keys
input_search.send_keys(Keys.CONTROL,'a')
input_search.send_keys(Keys.DELETE)

button_search=driver.find_element(By.XPATH,"//div[@class='nav-search-btn']")
button_search.click()

print(input_search.get_attribute("title"))
time.sleep(10)