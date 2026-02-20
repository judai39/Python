import asyncio
from pyppeteer import launch

# 5.高级特性解析

# 5.1 动态内容处理--无限滚动加载为例
async def scroll_to_bottom(page):
    while True:
        await page.evaluate('window.scrollBy(0,1000)')
        await asyncio.sleep(1)
        if await page.evaluate('document.documentElement.scrollTop >= document.body.scrollHeight-1000'):
            break

# 5.2 网络请求拦截--拦截并修改请求为例
async def intercept_request(page):
    await page.setRequestInterception(True)
    page.on('request',lambda req:asyncio.create_task(handle_request(req)))

async def handle_request(request):
    if request.url.endswith('.js'):
        await request.abort()#阻止js文件加载
    else:
        await request.continue_()

async def main():
    browser=await launch(headless=False,devtools=True)
    page=await browser.newPage()
    await page.goto('https://www.baidu.com',waitUntil='networkidle2')
    # await scroll_to_bottom(page)
    # await intercept_request(page)
    await browser.close()

loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())