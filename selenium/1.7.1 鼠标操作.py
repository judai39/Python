from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.bilibili.com")
element=WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//ul[@class='right-entry']/li[3][1]"))
)
# 创建ActionChain对象(和Alert()在同一个包中,说明键鼠操作和浏览器操作属于同一层级)
from selenium.webdriver.common.action_chains import ActionChains
actionChain=ActionChains(driver)
# 1.悬停鼠标(多用于下拉列表)
actionChain.move_to_element(element).perform()
# 2.双击鼠标
actionChain.double_click(element).perform()
# 3.单击鼠标

# cancle_element=driver.find_element(By.XPATH,"//div[@class='bili-mini-mask']/div[@class='bili-mini-content-wp']/div[@calss=bili-mini-close-icon]")
# （；´д｀）ゞ:直接查找动态元素没有查找到,因为异步的问题,没来得及加载出来就进行了查找,使用显性等待

cancle_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//div[@class='bili-mini-mask']/div[@class='bili-mini-content-wp']/div[@class='bili-mini-close-icon']"))
)

# 使用js语句直接操作dom返回元素也可以
# cancle_element = driver.execute_script("return document.querySelector('div.bili-mini-mask');")
actionChain.click(cancle_element).perform()

# 4.拖放操作
manga_element=driver.find_element(By.XPATH,"//div[@class='bili-header__bar']/ul[@class='left-entry']/li[@class='v-popover-wrap']")
search_input_element=driver.find_element(By.CLASS_NAME,"nav-search-content")
actionChain.drag_and_drop(manga_element,search_input_element).perform()
# 疑问? 必须要等待所有其他操作完成,否则登录的子页面会挡住拖放操作的进行,如何保证其他操作完成后等待一段时间再执行拖放操作


time.sleep(60)