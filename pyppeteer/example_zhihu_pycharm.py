# 实战案例--知乎反爬虫突破
# --to be continued

import asyncio
from pyppeteer import launch

async def scrape_zhihu():
    browser=await launch(headless=False)
    page=await browser.newPage()

    # 设置代理伪装
    await page.authenticate({'username':'proxy_user','password':'proxy_pass'})
    await page.evaluateOnNewDocument('''
        Object.defineProperty(navigator,'webdriver',{get:()=>false})
    ''')

    # 访问并登录
    await page.goto('https://www.zhihu.com/signin')
    # await page.click()
    await page.type('#acount','14792323948')
    await page.type('#password','DHY2522609443')
    await page.click('.SignFlow-submitButton')

    # 等待登录完成
    await page.waitForNavigation()

    # 抓取问题与回答
    questions=await page.querySelectorAll('.QuestionItem-title')
    for q in questions:
        print(await q.getProperties('textContent'))
    await browser.close()
loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(scrape_zhihu())