""" 异步上下文管理器
通过定义__aenter__()和__aexit__()方法来对async with语句中的环境进行控制。
"""
import asyncio


class AsyncContextManage:
    def __init__(self):
        # self.conn = conn 初始化连接
        pass

    async def do_something(self):
        # 异步执行某些操作
        return "去干活"

    async def __aenter__(self):
        # 异步连接数据库
        self.con = await asyncio.sleep(2)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭连接
        await asyncio.sleep(2)


# async with: 要放在async 函数里
async def fun():
    async with AsyncContextManage() as f:
        res = await f.do_something()
        print(res)


asyncio.run(fun())
