from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.bilibili.com")
element_input=driver.find_element(By.XPATH,"//div[@class='bili-header large-header']//input[@class='nav-search-input']")
element_input.send_keys("hello world")
time.sleep(2)
element_input.send_keys(Keys.CONTROL,'a')
time.sleep(2)
element_input.send_keys(Keys.CONTROL,'x')
time.sleep(2)
element_input.send_keys(Keys.CONTROL,'v')
time.sleep(10)