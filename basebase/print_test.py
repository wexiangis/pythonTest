
pInt = 123
pFloat = 123.456
pBool = True
pArray = 1,2,3

#coding=utf-8
'''
print方法的使用:
    print(*objects,sep="",end="\n",file=sys.stdout,flush=False)
'''
print(pInt,pFloat,pBool,pArray)
print(pInt,pFloat,pBool,pArray,sep="|",end=" this end\r\n")

name=input("your name is ")
print("XXXOOO -> ", name)
