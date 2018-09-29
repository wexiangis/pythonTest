#!/usr/bin/python3.4

f = open("./file/t.txt", "r+")

print(str(f.read()))

f.write("new line\r\n")

f.close()
