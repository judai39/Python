import asyncio
from pyppeteer import launch

# selenium中使用driver.execute_script()处理js逻辑
# pyppeteer中使用page.evaluate()处理js逻辑

async def main():
    browser=await launch(headless=False)
    page=await browser.newPage()
    await page.goto("https://www.bilibili.com")
    # 1.处理alert弹窗对象
    # 绑定监听弹窗事件
    # page.on('dialog',lambda dialog:asyncio.ensure_future(handle_dialog(dialog,"")))
    # await page.evaluate("alert('这是一个alert弹窗')")
    # await asyncio.sleep(10)

    # 2.处理prompt弹窗对象
    page.on('dialog',lambda dialog:asyncio.ensure_future(handle_dialog(dialog)))
    await page.evaluate("prompt('这是一个prompt弹窗')")
    # 手动接收
    # to be continue
    await asyncio.sleep(10)
    await browser.close()

async def handle_dialog(dialog):
    """处理浏览器弹窗"""
    print(f"弹窗类型:{dialog.type}")
    print(f"弹窗内容:{dialog.message}")
    # 自动接收
    # await dialog.accept("这是自动输入的内容")

loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())