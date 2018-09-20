#!/usr/bin/python3.4

def fun1(num) :
    "fun1"
    print("fun 1")
    num = 1
    return

def fun2(strs) :
    "fun2"
    print("fun 2")
    strs = "123"
    return

def fun3(lists) :
    "fun3"
    print("fun 3")
    lists[0] = 0
    return

def fun4(tuples) :
    "fun4"
    print("fun 4")
    del tuples
    return

def fun5(sets) :
    "fun5"
    print("fun 5")
    sets['new'] = "new one"
    return

num = 100
strs = '100'
lists = [10, 20, 30]
tuples = (10, 20, 30)
sets = {'d1' : "d1 value"}

fun1(num)
fun2(strs)
fun3(lists)
fun4(tuples)
fun5(sets)

print(num, strs, lists, tuples, sets)
