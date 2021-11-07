import random

import requests
import asyncio

"""
案例：asyncio+不支持异步的模块
"""


async def img(url):
    print("开始下载。。。。。")
    loop = asyncio.get_event_loop()
    # requests默认不支持异步
    fut = loop.run_in_executor(None, requests.get, url)
    response = await fut
    with open("img" + str(random.randint(1, 5)) + ".svg", mode="wb") as f:
        f.write(response.content)
    print("下载完成")


if __name__ == '__main__':
    url_list = [
        "https://infinityicon.infinitynewtab.com/assets/windmill.svg",
        "https://infinityicon.infinitynewtab.com/assets/windmill.svg",
        "https://infinityicon.infinitynewtab.com/assets/windmill.svg",
    ]
    tasks = [img(url) for url in url_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
