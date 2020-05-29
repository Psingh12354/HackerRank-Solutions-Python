from itertools import product
a=input().split()
a=list(map(int,a))
b=input().split()
b=list(map(int,b))
for i in product(a,b):
    print(i,end=" ")
