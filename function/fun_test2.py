#!/usr/bin/python3.4

def fun1(x, y) :
    print("x + y = ", x+y)
    return

# def fun2(key) :
#     print("key : ", key)
#     return

def fun2(**p) :
    print(str(p))
    return

def fun3(a, *b, **c) :
    print(a, b, c)
    return

def fun4(x) :
    def fun5(y) :
        print(x*y)
        return
    return fun5

def fun6(x) :
    print("fun6 : ", x)
    x -= 1
    return fun6(x) if x >= 0 else None

def fun7(a, b, c) :
    return str(a)+str(b)+str(c)

def fun8(a) :
    return a<5

t = (1, 2)
s = {'key' : "value"}

fun1(*t)
fun2(**s)
fun3(1, 2, 3, 4, b=5, c=6, d=7)
fun3(1)

f = fun4(2)
f(3)

fun6(3)

print(list(map(fun7, [1, 2, 3], ['a', 'b', 'c'], ['!', '@', '#'])))

print(list(filter(fun8, (1,5,3,7,9,3,7,5,4,1,8,4))))