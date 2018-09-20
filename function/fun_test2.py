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

t = (1, 2)
s = {'key' : "value"}

fun1(*t)
fun2(**s)
fun3(1, 2, 3, 4, b=5, c=6, d=7)
fun3(1)

