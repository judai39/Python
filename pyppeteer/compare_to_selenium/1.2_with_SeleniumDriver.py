# selenium是通过代码webdriver.Chrome(service=)查找本地的chrome内核驱动（本地配置在users/.chromedriver）
# selenium的chromedriver驱动要对应当前安装的chrome版本号，如果没有配置本地，将会自动下载当前版本的chromedriver

# pyppeteer和selenium一样，需要匹配版本号，也会自动下载匹配版本的chromium内核（本地配置在C:\Users\judai\AppData\Local\pyppeteer\pyppeteer\local-chromium\1181205[版本号]）
# 但是由于pyppeteer的自动匹配有些垃圾（具体表现为对应的版本号有时会被覆盖。。。）,所以chromium是手动配置的

import asyncio
from pyppeteer import launch

# pyppeteer需要重写协程代码，需要实现线程安全
async def main():
    # launch会自动加载pyppeteer下的chromium内核驱动文件
    browser=await launch()
    page=await browser.newPage()
    await page.goto('https://www.baidu.com')
    await browser.close()