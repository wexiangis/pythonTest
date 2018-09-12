#!/usr/bin/python3.4

pInt = 123
pFloat = 123.456
pBool = True
pArray = 1,2,3
pString='1234567890\n123'

#-*-coding:utf-8-*-
'''

print方法的使用:

print(*objects,sep="",end="\n",file=sys.stdout,flush=False)

'''
print(pInt,pFloat,pBool,pArray)
print(pInt,pFloat,pBool,pArray,sep="|",end=" this end\r\n")

print("----- string test -----")
print(pString[0])
print(pString[-2])
print(pString[3:5])
print(pString[5:])
print(pString*2)
print("----- string test end -----")

"this is a \N{dog}"

# name=input("your name is ")
# print("XXXOOO -> ", name)
