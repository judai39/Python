import asyncio
from pyppeteer import launch
import time
import random

async def main():
    browser=await launch(headlesss=False,devtools=True)
    page=await browser.newPage()
    await page.goto("https://www.bilibili.com")
    # 定位元素

    # # 1.通过page.xpath()定位
    # element_xpath=await page.xpath("//div[@class='bili-feed4']//div[@class='bili-header__bar']/div[1]/div[1]/form[1]/div[1]/input[1]")
    # # 这里的xpath为多重路径，element_xpath被默认封装成list
    # # 获取元素标签属性
    # preholder_value=await (await element_xpath[0].getProperty("title")).jsonValue()
    # print(preholder_value)


    # 2.递交元素(param1=css选择器 , param2=递交字段 , param3=延迟时间)
    await page.type('.nav-search-input',"to search content",{'delay':random.randint(0,5)}) 
    
    # # 3.通过page.querySelector(.class、#id)css选择器定位
    # element_querySelector=await page.querySelector(".nav-search-btn")
    # # 点击事件
    # await element_querySelector.click()
    # pages=await browser.pages()
    # await pages[1].bringToFront()
    # time.sleep(10)

    await browser.close()

loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())