import asyncio
import uvloop

"""
    替换默认的事件循环
"""

# 只加这一句就好了，后面的代码与之前的一样
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
...
asyncio.run(...)
