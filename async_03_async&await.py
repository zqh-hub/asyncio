"""
    通过async&await实现
"""
import asyncio


async def fun1():
    print(1)
    await asyncio.sleep(5)  # 遇到IO耗时，自动切换到其他任务。IO耗时：比如下载文件
    print(2)


async def fun2():
    print(3)
    await asyncio.sleep(5)  # 遇到IO耗时，自动切换到其他任务
    print(4)


tasks = [
    asyncio.ensure_future(fun1()),
    asyncio.ensure_future(fun2())
]
loop = asyncio.get_event_loop()     # 生成一个事件循环
loop.run_until_complete(asyncio.wait(tasks))  # 将任务放入"任务列表"
