#!/usr/bin/python3.4

from testPackage import out

class TC1 :

    __tC1_privateData = "tC1_privateData"

    def __init__(self) :
        print("TC1 init")
    
    def getPrivateData(self) :
        return self.__tC1_privateData


class TC(TC1, out.Output) :

    def __init__(self) :
        TC1.__init__(self)
        out.Output.__init__(self)
        print("TC init")


testClass = TC()

testClass.print("123")
testClass.setHead("print : ")
testClass.print("123")
testClass.print(testClass.getPrivateData())
