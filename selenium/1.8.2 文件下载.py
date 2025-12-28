from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# options参数携带下载路径
options=Options()

# !!!!!!!!!!!!!!!!!!这一段代码一定要放在下列添加参数代码下面执行才能生效
# options.add_experimental_option("prefs", { "download_restrictions": 0 })
# options.add_experimental_option("prefs", { "safebrowsing.enabled": False })
options.add_experimental_option("prefs", {
    "download.default_directory": "C:/Users/judai/Desktop",
    # 禁止弹出下载对话框
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
# 放在这里才能生效
# 禁用下载保护，允许下载所有类型的内容
options.add_experimental_option("prefs", { "download_restrictions": 0 })
options.add_experimental_option("prefs", { "safebrowsing.enabled": False })

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://sample.cat/zh/csv")
element_download=driver.find_element(By.XPATH,"//a[@class='btn btn-primary rounded-pill btn me-2']")
element_download.click()
time.sleep(100)