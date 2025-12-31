import unittest
from time import sleep
from ddt import ddt,data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import unittest.test

class TestBaidu(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Chrome(service=Service())