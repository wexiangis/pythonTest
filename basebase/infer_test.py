#!/usr/bin/python3.4

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']

d = {i : j for i in girls for j in boys if i[0] == j[0]}

print(str(d))


# import math
# d = {'pi' : 0, 'dir' : True}
# for i in range(1, 100000000, 2) : 
#     # print(i)
#     if d['dir'] :
#         d['pi'] += 1/i
#         d['dir'] = False
#     else :
#         d['pi'] -= 1/i
#         d['dir'] = True

# d['pi'] *= 4 
# print(str(d), " / ", math.pi)


