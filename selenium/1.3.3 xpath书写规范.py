#对应拓展--如何正确无误的书写xpath路径文本
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from asyncio import wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.bilibili.com")

# 基本定位--查找到该页面下所有...标签元素
input=driver.find_element(By.XPATH,"//input")

# 基本定位--查找到该页面下所有id为...的元素
username=driver.find_element(By.XPATH,"//*[@id='vite-legacy-polyfill']")

# 文本定位--精确匹配文本内容为"登录"的标签
login=driver.find_element(By.XPATH,"//*[text()='专栏']")

# 文本定位--模糊匹配文本内容为"数"的标签
shu=driver.find_element(By.XPATH,"//*[contains(text(),'数')]")

# 层级定位--父子层级定位
zhuanlan=driver.find_element(By.XPATH,"//a[@class='channel-link__right']/span[1]")
    #如何通过子节点查找父节点?
zhuanlan_parent1=driver.find_element(By.XPATH,"//a[@class='channel-link__right']/span[1]/..") 
zhuanlan_parent2=driver.find_element(By.XPATH,"//a[@class='channel-link__right']/span[1]/parent::*") 
print(zhuanlan_parent2.tag_name,zhuanlan_parent2.tag_name)

# 层级定位--祖先层级定位
huodong_fukuzatsu=driver.find_element(By.XPATH,"//div[@class='bili-header__channel']/div[2]/div[2]/a[3]/span[1]")
    # 这样太复杂了...
huodong=driver.find_element(By.XPATH,"//div[@class='bili-header__channel']//span[text()='活动']")

# 逻辑运算定位--与运算查找
input_and=driver.find_element(By.XPATH,"//input[@class='nav-search-input' and @maxlength='100']")

# 逻辑运算定位--或运算查找
input_or=driver.find_element(By.XPATH,"//input[@class='nav-search-input' or @maxlength='120']")

# 轴定位--兄弟节点定位
# 假设页面结构为 
# <div>
#     <p id="target">目标元素</p>
#     <span>兄弟元素</span>
# </div>
zhibo_following=driver.find_element(By.XPATH,"//div[@class='right-channel-container']/div[2]/a[2]/following-sibling::a[1]")
print("直播标签之后的第一个兄弟节点为:",zhibo_following.text)
zhibo_preceding=driver.find_element(By.XPATH,"//div[@class='right-channel-container']/div[2]/a[2]/preceding-sibling::a[1]")
print("直播标签之前的第一个兄弟节点为:",zhibo_preceding.text)
# following-sibling 轴表示选取当前节点之后的所有兄弟节点，[1]表示选取第一个。
# 定位<svg>标签后的元素会失败?