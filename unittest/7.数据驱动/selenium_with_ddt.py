import unittest
from time import sleep
from ddt import ddt,data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest.test
from selenium.webdriver.common.by import By

@ddt
class TestBaidu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(service=Service('C:/Users/judai/.chromedriver/chromedriver143/chromedriver.exe'))
        self.driver.get("https://www.baidu.com")

    def tearDown(self) -> None:
        sleep(3)
        self.driver.quit()

    #单一参数
    @data('测试','开发')
    def test_01(self,name):
        self.driver.find_element(By.ID,"chat-textarea").send_keys(name)
        self.driver.find_element(By.ID,"chat-submit-button").click()

if __name__=='__main__':
    unittest.main(verbosity=2)