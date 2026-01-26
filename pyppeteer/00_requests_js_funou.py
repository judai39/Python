import requests

from pyquery import PyQuery as pq
# PyQuery 是一个 Python 库，提供类似 jQuery 的 API，用于解析和操作 HTML 和 XML 文档
# (本例用于解析网页文件中class=quote)

url=url = 'http://quotes.toscrape.com/js/'

response=requests.get(url)

doc=pq(response.text)

print('Quotes:',doc('.quote').length)

# 结果为0,由于该网页需要js渲染,我们所看到的网页内容都要经过js渲染,因此不可能直接爬取

# -->使用pyppeteer操作chromium无头浏览器内核,实现"渲染"
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq
async def main():
    # launch()参数
    #  healess:默认true(无头浏览器模式)
    # devtools:默认false(关闭调试工具)
    browser=await launch(headless=False,devtools=True)
    page=await browser.newPage()
    await page.goto("http://quotes.toscrape.com/js/")
    doc=pq(await page.content())
    print('Quotes:',doc('.quote').length)
    await browser.close()
loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())
# 结果为10,成功加载