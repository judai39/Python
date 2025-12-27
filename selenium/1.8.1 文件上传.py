from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.freeconvert.com/zh/jpg-converter")
input_element=driver.find_element(By.XPATH,"//input[@type='file' and @id='file']")
input_element.send_keys("C:/Users/judai/Desktop/img.jpg")
time.sleep(60)