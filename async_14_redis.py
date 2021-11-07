"""
案例：异步操作redis
"""
import asyncio
import aioredis


async def execute(address, password):
    print("开始执行", address)
    # IO操作：创建redis连接
    redis = await aioredis.create_redis(address, password)
    # IO操作：在redis中设置哈希值car
    await redis.hmset_dict('car', key1=1, key2=2, key3=3)
    # IO操作：获取值
    res = await redis.hgetall('car', encodings="utf-8")
    redis.close()
    # IO操作：关闭redis连接
    await redis.wait_closed()
    print("结束", address)


tasks = [
    execute("...", "..."),
    execute("...", "..."),
]
asyncio.run(asyncio.wait(tasks))
