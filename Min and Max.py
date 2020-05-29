import numpy
n, m=map(int,input().split(' '))
my_arr=numpy.array([input().split(' ') for i in range(n)],int)
print(numpy.max(numpy.min(my_arr,axis=1)))


