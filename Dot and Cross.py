import numpy
n = int(input())
list1 = numpy.array([input().split() for i in range(n)], int)
list2 = numpy.array([input().split() for i in range(n)], int)
print(numpy.dot(list1,list2))
