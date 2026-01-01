import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    # 设置正确的驱动路径
    service = ChromeService(executable_path="C:/Users/judai/.chromedriver/chromedriver143/chromedriver.exe")
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_baidu_search(browser):
    browser.get("https://www.baidu.com")
    search_box = browser.find_element(By.NAME, "wd")
    search_box.send_keys("Selenium")
    search_box.submit()
    assert "Selenium" in browser.title