#对应菜鸟Selenium教程中的Selenium隐式,显示等待机制
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.baidu.com")
# 1.设置隐式等待(所有元素的处理都会经过10s)
# driver.implicitly_wait(10)
# element=driver.find_element(By.ID,"form")
# 缺点:
# 全局性等待，可能会导致不必要的等待时间。
# 无法处理某些复杂的等待条件，例如等待元素变为可点击状态。



# 2.设置显式等待
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
element=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,"form"))
    # EC.presence_of_element_located()  等待元素出现在dom中
    # EC.visibility_of_element_located()    等待元素出现在dom中并且可见
    # EC.element_to_be_clickable()  等待元素可点击
    # Ec.text_to_be_present_in_element()    等待元素的文本包含指定文本
)
# 等待元素的文本包含指定文本
element_wait=WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.XPATH,"//div[@class='panel-list_8jHmm']/div[3]/span[1]"),"AI文本")
)
driver.quit()
# 显示等待灵活度高可以处理复杂的等待条件

