#对应菜鸟Selenium教程中的Selenium Driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.bilibili.com")
# driver.maximize_window()
# driver.set_window_size(1024,768)
# driver.fullscreen_window()
# # driver.close()
# driver.quit()

driver.refresh()
title=driver.title
print(title)

url=driver.current_url
print(url)

driver.get("https://www.baidu.com")
driver.back()
driver.forward()