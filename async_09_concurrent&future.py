import asyncio
import time
from concurrent.futures import Future

""" concurrent.futures.Future
    concurrent.futures.Future:使用线程池、进程池实现异步操作时用到。
    这个Future与async的Future没有任何关系，但是在写代码中：如果一个第三方模块不支持async，就只能使用线程池
"""


def fun1():
    print("1")
    time.sleep(2)
    print("2")
    return "普通函数1"


def fun2():
    print("3")
    time.sleep(2)
    print("4")
    return "普通函数2"


async def main():
    loop = asyncio.get_running_loop()
    fut1 = loop.run_in_executor(None, fun1)  # 将普通函数传入，返回async.Future对象
    fut2 = loop.run_in_executor(None, fun2)
    res1 = await fut1
    print(res1)
    res2 = await fut2
    print(res2)


asyncio.run(main())
