import numpy
A= numpy.array([input().split() for i in range(int(input().split()[0]))],int)
print(A.transpose())
print(A.flatten())
