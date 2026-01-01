import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os.path

class ScreenShotTest(unittest.TestCase):
    def setUP(self):
        self.driver=webdriver.Chrome(Service('C:/Users/judai/.chromedriver/chromedriver143/chromedriver.exe'))
        self.driver.get("https://bilibili.com")
        self.driver.maximize_window()

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    def test_01(self):
        driver=self.driver
        try:
            driver.find_element(By.ID,"id")
        except:
            self.saveScreenShot(self,driver,"shot.png")

    def saveScreenShot(self,driver,filename):
        if not os.path.exists("./img"):
            os.makedirs("./img")
        now=time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
        driver.get_screenshot_as_file("./img/",now,"-",filename)
        time.sleep(3)


if __name__=="__main__":
    unittest.main(verbosity=2)