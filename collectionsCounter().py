import collections
x=int(input())
sizes = collections.Counter(map(int,input().split()))
n=int(input())
MonEar=0
for i in range(n):
    (size,price)=map(int,input().split())
    if sizes[size]>0:
        sizes[size]-=1
        MonEar+=price
print(MonEar)
