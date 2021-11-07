import asyncio

""" 
当事件循环在task生成之后才有时
"""


async def fun1():
    print("1")
    await asyncio.sleep(2)
    print("2")
    return "返回值1"


async def fun2():
    print("3")
    await asyncio.sleep(2)
    print("4")
    return "返回值2"


task_list = [
    fun1(),
    fun2()
]

done, pending = asyncio.run(asyncio.wait(task_list, timeout=None))
print(done)
