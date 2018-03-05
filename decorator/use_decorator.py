from decorator import my_decoratorA, my_decoratorB
@my_decoratorA
def my_functionA():
    print("my function A do something!")

@my_decoratorB
def my_functionB():
    print("my function B do something!")

if __name__ == "__main__":
    my_functionA()
    print(my_functionA)
    print("help:",help(my_functionA))
    my_functionB()
    print(my_functionB)
    print("help:",help(my_functionB))

