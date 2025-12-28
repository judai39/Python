# 开启主机hub测试主控:java -jar selenium-server-4.39.0.jar hub
# 开启测试端node:java -jar selenium-server-4.39.0.jar node --hub http://localhost:4444
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

driver=webdriver.Chrome(service=Service('C:/Users/judai/.chromedriver/chromedriver143/chromedriver.exe'))

# 设置DesiredCapabilities
capAbilities=DesiredCapabilities.CHROME.copy()
capAbilities['platform']='WINDOWS'
capAbilities['version']='latest'

# 连接到Selenium grid hub主控端
driver=webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=webdriver.ChromeOptions()
)

#执行测试
driver.get("https://www.bilibili.com")
print(driver.title)
# driver.quit()