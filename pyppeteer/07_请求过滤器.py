import asyncio
from pyppeteer import launch

async def main():
    browser=await launch(headless=False,args=['--disable-inforbars'])
    browser=await browser.createIncognitoBrowserContext()#新建一个chromium任务
    page=await browser.newPage()
    # 开启请求拦截器
    await page.setRequestInterception(True)
    # 设置请求拦截器
    page.on('request',lambda req:asyncio.ensure_future(intercept_request(req)))
    # 设置响应拦截器
    page.on('response',lambda response:asyncio.ensure_future(intercept_response(response)))
    await page.goto('https://www.baidu.com/')
    print(await page.title())
    await asyncio.sleep(5000)

async def intercept_request(req):
    url=req.url
    if url=='https://fanyi.baidu.com/':
        # 用给定内容响应请求
        await req.respond({'status':200,'body':'welcome to new page'})
    elif url=='https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png':
        print('已过滤该图片')
        # 终止intercept_request()协程(要不然图片会一直加载不出来,服务器一直请求,就死循环了)
        await req.abort()
    elif url=='https://www.qq.com/':
        # 跳转请求
        await req.continue_({'url':'https://www.tencent.com/zh-cn/','method':'GET'})
    else:
        # 保持请求
        await req.continue_()

# 响应拦截器
async def intercept_response(response):
    if response.status==200 and response.url=='https://www.baidu.com/':
        text=await response.text()
        print(text)
    if '/api/movie' in response.url and response.status==200:
        json_data=await response.json()
        print(json_data)

loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())