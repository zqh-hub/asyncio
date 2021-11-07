"""
案例：异步操作mysql
"""
import asyncio
import aiomysql


async def execute(address, password):
    print("开始执行", address)
    # IO操作：创建mysql连接
    conn = await aiomysql.connect(host="", port=3306, user="", password="")
    # IO操作
    cur = await conn.cursor()
    # IO操作：获取值
    await cur.execute("select * from xxxxx")
    res = await cur.fetchall()
    print(res)
    # IO操作：关闭redis连接
    await cur.close()
    conn.close()
    print("结束")


tasks = [
    execute("...", "..."),
    execute("...", "..."),
]
asyncio.run(asyncio.wait(tasks))
