import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

class GithubTestCase(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome(service=Service('C:/Users/judai/.chromedriver/chromedriver143/chromedriver.exe'))
        self.addCleanup(self.browser.quit())

    def test_search(self):
        self.browser.get("https://github.com")
        search_box_elem=self.browser.find_element(By.XPATH,"//input[@name='q']")
        search_box_elem.send_keys('Selenium'+Keys.RETURN)

        first_result_elem=self.browser.find_element(By.XPATH,'//ul[@class="repo-list"]/li//div[@class="d-flex"]//a')
        first_result_elem.click()

        WebDriverWait(self.browser,10).until(EC.presence_of_element_located((By.ID,"code-tab")))

        self.assertIn('Selenium',self.browser.title)

if __name__=='__main__':
        unittest.main(verbosity=2)