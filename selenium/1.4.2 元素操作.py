#对应菜鸟Selenium教程中的Selenium元素操作
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.imgdiet.com/zh-CN/convert")

element_upgrade=driver.find_element(By.XPATH,"//button[@class='btn file-uploads-btn hi-btn']/input[1]")
element_upgrade.send_keys("C:/Users/judai/Pictures/Camera Roll/96956767_p7.jpg")
