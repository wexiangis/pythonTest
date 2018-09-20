#!/usr/bin/python3.4

for i in range(10, 0, -1) :
    if i+i >= i*i :
        print("result : ", i)
        break
else :
    print("result : None")
