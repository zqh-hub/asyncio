"""
asyncio.Future,是Task的基类
"""
import asyncio


async def test01():
    # 获取事件循环
    loop = asyncio.get_running_loop()
    # 创建一个任务(Future),这个任务什么也不干
    future = loop.create_future()
    # 因为它什么也没干，所以一直没有结果，就会椰子汁等待下去
    await future


# asyncio.run(test01())

async def set_after(future):
    await asyncio.sleep(2)
    future.set_result("结果")


async def main():
    # 获取事件循环
    loop = asyncio.get_running_loop()
    # 创建一个任务(Future)
    future = loop.create_future()
    # 创建一个Task对象，并将值给Future
    await loop.create_task(set_after(future))
    # 等待future获取值，最终终止
    res = await future
    print(res)


asyncio.run(main())
