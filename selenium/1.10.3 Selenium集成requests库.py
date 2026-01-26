from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import requests

service = ChromeService(executable_path="C:/Users/judai/.chromedriver/chromedriver143/chromedriver.exe")
options=webdriver.ChromeOptions()
driver=webdriver.Chrome(service=service,options=options)

driver.get("https://www.bilibili.com")
search_input=driver.find_element(By.XPATH,'//div[@class="nav-search-content"]/input[@class="nav-search-input"]')
search_input.send_keys("selenium")
search_button=driver.find_element(By.XPATH,'//div[@class="nav-search-btn"]')
search_button.click()

from requests_html import HTMLSession
# 需要手动安装,配置pyppeteer的安装路径
# 使用以下代码输出所需pyppeteer版本号
# import pyppeteer.chromium_downloader
# print('默认版本是：{}'.format(pyppeteer.__chromium_revision__))
# print('可执行文件默认路径：{}'.format(pyppeteer.chromium_downloader.chromiumExecutable.get('win64')))
# print('win64平台下载链接为：{}'.format(pyppeteer.chromium_downloader.downloadURLs.get('win64')))
session=HTMLSession()
response=session.get('https://search.bilibili.com/all?keyword=selenium')
response.html.render()
assert "selenium" in response.text
import time
time.sleep(10)