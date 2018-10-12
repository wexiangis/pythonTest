#!/usr/bin/python3.4

class tC :

    count = 0

    def __init__(self) :
        tC.count += 1

    def setCount(self, var) :
        self.count = var

    def getCount(self) :
        return self.count


t1 = tC()
t2 = tC()

print(t1.getCount())
print(t2.getCount())
print(tC.count)

t1.setCount(10)
print(t1.getCount())
print(t2.getCount())
print(tC.count)

t2.setCount(20)
print(t1.getCount())
print(t2.getCount())
print(tC.count)

print(getattr(tC, "setCount", "None"))
print(getattr(t1, "setCount", "None"))
print(getattr(t2, "setCount", "None"))
print(t1.__dict__)
print(dir(t1))