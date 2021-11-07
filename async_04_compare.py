import asyncio
import random
import aiohttp

import requests

"""
比较普通方式和协程的方式下载文件
"""


# 普通方式
def general(img_url):
    print("开始下载")
    response = requests.get(img_url)
    with open("img" + str(random.randint(1, 5)) + ".svg", "wb") as f:
        f.write(response.content)
    print("下载完成")


async def async_await(img_url):
    async with aiohttp.ClientSession() as session:
        print("开始下载")
        async with session.get(img_url, verify_ssl=False) as response:
            content = await response.content.read()
            with open("img" + str(random.randint(1, 5)) + ".svg", mode="wb") as f:
                f.write(content)
        print("下载完成")


async def main():
    url_list = [
        "https://infinityicon.infinitynewtab.com/assets/windmill.svg",
        "https://infinityicon.infinitynewtab.com/assets/windmill.svg",
        "https://infinityicon.infinitynewtab.com/assets/windmill.svg",
    ]
    tasks = [asyncio.create_task(async_await(url)) for url in url_list]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # general("https://infinityicon.infinitynewtab.com/assets/windmill.svg")
    asyncio.run(main())
