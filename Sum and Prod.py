import numpy
n,m=map(int,input().split(' '))
my_arr = numpy.array([input().split() for i in range(n)], int)
print(numpy.prod(numpy.sum(my_arr, axis = 0)))


