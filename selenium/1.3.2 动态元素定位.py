#对应拓展--如何查找到bilibili中的登录动态页面中的取消div元素
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from asyncio import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.bilibili.com")
element=driver.find_element(By.XPATH,"//ul[@class='right-entry']/li[3][1]")
actionChain=ActionChains(driver)
actionChain.move_to_element(element).perform()
actionChain.click(element).perform()

# 1.使用显式等待（Explicit Wait）
    #显式等待是处理动态元素的最常用方法。通过设置等待条件，直到元素满足特定状态（如可点击、可见等）才执行操作，从而避免因元素未加载完成而导致的定位失败。
cancle_element1=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//div[@class='bili-mini-mask']/div[@class='bili-mini-content-wp']/div[@class='bili-mini-close-icon']"))
)

# 2. 相对定位器（Relative Locators）
# Selenium 4引入了相对定位器，可以通过元素之间的相对位置关系进行定位，这对于动态生成的元素尤其有用。
from selenium.webdriver.support.relative_locator import with_tag_name

element_password=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//div[@class='bili-mini-mask']/div[@class='bili-mini-content-wp']/div[@class='bili-mini-login-right-wp']/div[@class='login-pwd-wp']/form[@class='tab__form']/div[@class='form__item']"))
)
element_email=driver.find_element(with_tag_name("input").above(element_password))

# 3.css选择器

# 4.xpath轴定位

# 5.处理动态id
# CSS选择器部分匹配
# driver.find_element(By.CSS_SELECTOR, "div[class^='dynamic-prefix']")
# XPath部分匹配
# driver.find_element(By.XPATH, "//div[contains(@id, 'dynamic-part')]")

# 6.使用js直接操作dom
cancle_element2=driver.execute_script("return document.querySelector('div.bili-mini-mask')")


time.sleep(60)