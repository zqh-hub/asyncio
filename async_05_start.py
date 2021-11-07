import asyncio

""" 入门 
    协程函数，被async关键字修饰的函数  async def
    协程对象，协程函数()
"""


async def fun():
    print("我就是协程函数")


task = fun()  # 注意：此时函数里的代码并没有执行，只是变成了协程对象

# 事件循环，运行协程。3.7之前的版本
loop = asyncio.get_event_loop()
loop.run_until_complete(task)

# asyncio.run(task)  python 3.7之后的版本
