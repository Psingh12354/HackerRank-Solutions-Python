import numpy
n, m=map(int,input().split(' '))
my_arr=numpy.array([input().split() for i in range(n)],int)
numpy.set_printoptions(legacy='1.13')
print( numpy.mean(my_arr, axis=1))
print( numpy.var(my_arr, axis=0))
print(( numpy.std(my_arr, axis=None)))
