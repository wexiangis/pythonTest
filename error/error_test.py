#!/usr/bin/python3.4

try :
    print(10/2)
except ZeroDivisionError as e :
    print(e)
else :
    print("nice code !!")
finally :
    print("finally")
