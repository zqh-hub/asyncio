import asyncio

""" await 
    await + 可等待对象(协程对象、Future、Task对象)
"""


async def util_fun():
    print("start")  # 第3步
    # asyncio.sleep(2)暂时代替"可等待对象"
    await asyncio.sleep(2)  # 第4步，等待2秒
    print("end")  # 第5步
    return "返回值"  # 第6步


async def fun():
    # 注意，这里有两个await,他们是依次执行的，执行到第一个时，会等待，直到第一个结束才会执行第二个
    res_01 = await util_fun()  # 第2步去执行utils_fun
    print(res_01)
    res_02 = await util_fun()  # 第7步
    print(res_02)


asyncio.run(fun())  # 第1步
