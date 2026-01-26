import asyncio
from pyppeteer import launch

async def main():
    browser=await launch()
    page=await browser.newPage()
    await page.goto('https://www.baidu.com')
    await page.screenshot({'path':r'C:\Users\judai\Desktop\example.png'})
    # 返回第一个a标签的文本内容
    element_text = await page.evaluate('document.querySelector("a").textContent')
    print(element_text)
    # 等待5秒
    await page.waitFor(5000) 
    await browser.close()

# 当前python版本过高,使用下列新代码
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
# 旧版本的为loop=asyncio.get_event_loop()

# 运行
loop.run_until_complete(main())