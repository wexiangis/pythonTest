#!/usr/bin/python2.7

from ctypes import *

class Lib_Struct(Structure):
	_fields_ = [("i", c_int),("d", c_double),("str", c_char * 17)]

if __name__ == "__main__":

    demo = cdll.LoadLibrary('./demo.so')

    demo.fun.restype = c_int
    demo.fun.argtypes = (c_int, c_double)
    demo.fun_io_struct.argtypes = [Lib_Struct]
    demo.fun_io_struct.restype = Lib_Struct
    demo.fun_io_struct_point.argtypes = [POINTER(Lib_Struct)]
    demo.fun_io_struct_point.restype = POINTER(Lib_Struct)

    res1 = demo.fun(1, 1.2345678)
    print res1

    arg1 = Lib_Struct(i = 10, d = 1.11111111, str = 'abcdefg')
    res2 = demo.fun_io_struct(arg1)
    print res2.i, res2.d, res2.str

    res3 = demo.fun_io_struct_point(res2)
    print res3.contents.i, res3.contents.d, res3.contents.str