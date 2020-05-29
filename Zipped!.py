N, X = map(int,input().split(' '))
list1 = []
for subject in range(X):
    list1 += [map(float,input().split())]
for Marks in zip(*list1):    
    print(sum(Marks)/X)
