#对应菜鸟Selenium教程中的Selenium元素定位
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from asyncio import wait
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.bilibili.com")

# 类名查找
element_class=driver.find_element(By.CLASS_NAME,"nav-search-input")

# 使用xpath相对定位查找元素(多用于没有id,有class的元素定位)
element_xpath=driver.find_element(By.XPATH,"//div/div[@class='bili-feed4']//div[@class='bili-header__bar']/div[1]/div[1]/form[1]/div[1]/input[1]")

# id查找
element_id=driver.find_element(By.ID,"i_cecream")

# 使用css选择器相对定位查找所有div中id为i_ceream的元素
element_css=driver.find_element(By.CSS_SELECTOR,"form#nav-searchform")

# 通过链接文本查找(<a href...>链接文本</a>)
element_text=driver.find_element(By.LINK_TEXT,"番剧")

# 通过父元素查找该父元素下的所有子元素
# son_elements=parent_element.find_elements(By.TAG_NAME,"...")

# （；´д｀）ゞ:如下所示,将所有ytd-playlist-video-render标签查找结果合并为数组,在数组中查找对应元素标签的</a>
# ----错误返回,所有print结果均为第一个数组元素中的啊</a>内容
    # vedio_div_list=spicify_content_div.find_elements(By.XPATH,"//ytd-playlist-video-renderer[@class='style-scope ytd-playlist-video-list-renderer']")
    # for element in vedio_div_list:
    # print(element.find_element(By.XPATH,"//a[@id='video-title']").get_attribute("title"))
    # time.sleep(1)
# 问题处在第三行的xpath查找语句,使用//a[...]会返回当前driver的根标签查找的第一个元素,对应第一个数组元素的内容,需要用.//a[...]表示当前路径查找而不是全局文档查找