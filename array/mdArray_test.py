#!/usr/bin/python3.4

# import numpy as np

ar = [[0, 1], [3, 4, 5]]
print(repr(ar))
ar[1][1] = 9
print(repr(ar))

ar = [1, 2, 3]*2
print(repr(ar))
ar[1] = 9
print(repr(ar))

ar = [[1, 2, 3]]*2
print(repr(ar))
ar[1][1] = 9
print(repr(ar))

ar = [ [0]*3 for i in range(2) ]
print(repr(ar))
ar[1][1] = 9
print(repr(ar))


ar = [ [ [i] for i in range(2) ] for j in range(3) ]
print(repr(ar))
ar[2][1][0] = 9
print(repr(ar))

ar = [ 1, [2, 3], [ [3, 4, 5], [ [6, 7, 8], [9, 10, 11] ] ] ]
print(repr(ar))
ar[0] = 101
ar[1][0] = 102
ar[2][0][0] = 103
ar[2][1][0][0] = 104
print(repr(ar))
