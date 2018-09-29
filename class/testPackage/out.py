#!/usr/bin/python3.4

class Output :

    __name = "Output"

    head = "out : "

    def __init__(self) :
        print(self.__name, " init")

    def print(self, value) :
        print(self.head, value)
    
    def setHead(self, value) :
        self.head = value

