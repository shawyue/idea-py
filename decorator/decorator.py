# _*_ coding:utf-8 _*_

def my_decoratorA(func):
    def wrapper(*args, **kwds):
        print("wrapper do something!")
        re = func(*args, **kwds)
        print("wrapper do something!")
        return re
    return wrapper

from functools import wraps
def my_decoratorB(func):
    @wraps(func)
    def wrapper(*args, **kwds):
        print("wrapper do something!")
        re = func(*args, **kwds)
        print("wrapper do something!")
        return re
    return wrapper
