"""
    通过asyncio实现
"""
import asyncio


def fun1():
    print(1)
    yield from asyncio.sleep(2)
    print(2)


def fun2():
    print(3)
    yield from asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(fun1()),
    asyncio.ensure_future(fun2())
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
