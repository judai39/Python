import asyncio
from pyppeteer import launch

async def main():
    # 1.启动和关闭browser
    browser = await launch(headless=False,devtools=True)
    # 2.导航与截图
    page=await browser.newPage()
    await page.goto('https://www.baidu.com',waitUntil='networkidle2')
    await page.screenshot({'path':r'C:\Users\judai\Desktop\screenshot.png','fullPage':True})
    # 2.1 切换标签页
    pages=await browser.pages()
    await pages[0].bringToFront()
    await pages[1].bringToFront()
    # 3.执行JavaScript(selenium所缺失的)
    dimension=await page.evaluate('''()=>{
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight
        }                              
    }
    ''')
    print(dimension)
    # 4.元素交互
    # await page.type('#username','my_user')
    await page.click("#chat-submit-button",delay=100)
    # await page.select("#country","US")
    await browser.close()

loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())