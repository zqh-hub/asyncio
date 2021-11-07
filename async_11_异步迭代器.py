""" 异步迭代器
什么是异步迭代器
实现了__aiter__()和__anext__()方法的对象。__anext__必须返回一个awaitable对象。
async for会处理异步迭代器的__anext()方法所返回的可等待对象，直到其引发一个StopAsyncIteration异常。

什么是异步可迭代对象
可在async for语句中被使用的对象。必须通过它的__aiter__()方法返回一个asynchronous iterator。
"""
import asyncio


class Reader:
    """
        自定义迭代器
    """

    def __init__(self):
        self.count = 0

    async def readline(self):
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = self.readline()
        if val is None:
            raise StopAsyncIteration
        return val


# async for:要放入async函数中
async def fun():
    obj = Reader()
    async for item in obj:
        print(item)


asyncio.run(fun())
