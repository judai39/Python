import asyncio
from pyppeteer import launch
import time
import random

async def main():
    browser=await launch(headless=False)
    time.sleep(3)
    page=await browser.newPage()
    await page.goto('https://www.bilibili.com')
    # 1.鼠标事件
    # 鼠标悬浮在元素上-page.hover()
    await page.hover('.nav-search-btn')

    # 鼠标的按下，移动，松开(常用于拖动操作)
    # await page.mouse.down()
    # await page.mouse.move(2000,0,{'delay':random.randint(1000,2000)})#第一个参数x轴，第二个参数y轴
    # await page.mouse.up()


    # 2.键盘事件
    asyncio.sleep(3)
    await page.type('.nav-search-input','to be continue',{"delay":random.randint(0,5)})
    # 回车
    await page.keyboard.press('Enter')
    time.sleep(5)


    await browser.close()

loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())
