#!/usr/bin/python3.4

# array=[8,4,9,1,0,2,5,6,7,3]
# array=[0,1,2,3,4,5,6,7,8,9]
array=[9,8,7,6,5,4,3,2,1,0]
print(array, "\n")

print("排序测试 1:")
circleCount=0
actCount=0
for i in range(0, len(array)):
    for j in range(i+1, len(array)):
        circleCount += 1
        actCount += 1
        if array[i] > array[j]:
            actCount += 1
            array[i], array[j] = array[j], array[i]
print(array, "数据量:{0}, 循环次数:{1}, 操作次数:{2}\n".format(len(array), circleCount, actCount))


print("排序测试 2: 冒泡排序")
circleCount=0
actCount=0
for i in range(0, len(array)-1):
    for j in range(0, len(array)-1):
        circleCount += 1
        actCount += 1
        if array[j] > array[j+1]:
            actCount += 1
            array[j], array[j+1] = array[j+1], array[j]
print(array, "数据量:{0}, 循环次数:{1}, 操作次数:{2}\n".format(len(array), circleCount, actCount))
