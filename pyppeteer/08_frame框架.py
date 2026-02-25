import asyncio
from pyppeteer import launch

async def main():
    browser=await launch(headless=False,args=['--disable-inforbars'])
    browser=await browser.createIncogniteBrowserContext()
    page=await browser.newPage()
    await page.goto("https://bilibili.com")
    # 针对frame框架的操作

    # 获取所有的frame 
    frame_list=page.frames
    # 获取当前页面的标题(以下三种)
    print(await frame_list[0].title())#有点像page.xpath(...)[0]
    print(await page.mainFrame.title())
    print(await page.title())

    await asyncio.sleep(10)

loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())