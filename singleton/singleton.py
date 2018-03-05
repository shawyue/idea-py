# _*_ coding:utf-8 _*_
#方法一
class SingletonA(object):
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(SingletonA, cls).__new__(cls, *args, **kw)  
        return cls._instance  
 
class MyClassA(SingletonA):  
    a = 1

#方法二
class SingletonB(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonB, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
 
 
class MyClassB(metaclass=SingletonB):
    pass



#方法四
from functools import wraps
 
def singletonD(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance
 
@singletonD
class MyClassD(object):
    a = 1

if __name__ == "__main__":
    classA = MyClassA()
    classB = MyClassA()
    print("classA==classB:",classA == classB, "classA is classB:",classA is classB)
    print("classA id:", id(classA), "classB id:", id(classB))

    classC = MyClassB()
    classD = MyClassB()
    print("classC==classD:",classC == classD, "classC is classD:",classC is classD)
    print("classC id:", id(classC), "classD id:", id(classD))

    #方法三
    from singletonC import singleton_class as classE
    from singletonC import singleton_class as classF

    print("classE==classF:",classE == classF, "classE is classF:",classE is classF)
    print("classE id:", id(classE), "classF id:", id(classF))


    classG = MyClassD()
    classH = MyClassD()
    print("classG==classH:",classG == classH, "classG is classH:",classG is classH)
    print("classG id:", id(classG), "classH id:", id(classH))




