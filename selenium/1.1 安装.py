#对应菜鸟Selenium教程中的Selenium安装
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

#查找并下载符合当前浏览器版本的webdriver驱动版本
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.baidu.com')
# time.sleep(2)

button=driver.find_element('id','chat-submit-button')
button.click()
print(button.text)
#强行等到页面加载完成10s
wait = WebDriverWait(driver, 10)

#问题:页面按钮点击完成后对象直接关闭,如何持续化?
import time
time.sleep(60)
#并非闪退,selenium执行代码之后会执行浏览器的默认行为,firefox的默认行为不是关闭浏览器,但是edge,chorme的默认行为是关闭浏览器