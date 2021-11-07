import asyncio

""" task  
    3.7之前：asyncio.ensure-future()
    3.7之后：asyncio.create_task() 
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


# main的作用就是将task对象添加到事件循环中
async def main():
    print("开始main")
    # 将多个task对象放入列表中
    task_list = [
        asyncio.create_task(fun1(), name="n1"),  # create_task(协程对象)：生成task对象。name：给task起名字
        asyncio.create_task(fun2(), name="n2")
    ]
    done, pending = await asyncio.wait(task_list, timeout=None)  # asyncio.wait：读取task对象列表，并返回done, pending
    print(done)


asyncio.run(main())
'''
这里的 asyncio.run 相当于：
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

也就是说，在先 get_event_loop(),从而得到事件循环，然后再将task对象添加到时间循环中。先有事件循环再添加task
但是还有一种情况是，还没有事件循环----->async_07_task2.py
'''
