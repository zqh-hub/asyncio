from greenlet import greenlet

"""
    通过greenlet实现
"""


def fun1():
    print("1")  # 第2步，输出1
    g2.switch()  # 第3步，切换到fun2,并保存这个切换点a
    print("2")  # 第6步，由fun2的第5步切换点b切换此，输出2
    g2.switch()  # 第7步，切换到fun2,并保存切换点c


def fun2():
    print(3)  # 第4步，由fun1的第3步切换到此，输出3
    g1.switch()  # 第5步，切换到fun1的切换点a,并保存切换点b
    print(4)  # 第8步，由fun1第7步的切换点c切换到此，输出4


g1 = greenlet(fun1)
g2 = greenlet(fun2)

g1.switch()  # 第1步，执行fun1函数
