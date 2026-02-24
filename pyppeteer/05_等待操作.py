import asyncio
from pyppeteer import launch

async def main():
    browser=await launch()
    # 1.设置固定等待
    await asyncio.sleep(5)
    page=await browser.newPage()
    await page.goto('https://www.bilibili.com')
    # 2.设置显示等待
    await page.waitForSelector('.nav-search-input')
    element=await page.querySelector('.nav-search-input')

    await browser.close()

loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())
    