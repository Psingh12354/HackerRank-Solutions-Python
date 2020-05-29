n=int(input())
list1=set(map(int,input().split(' ')))
m=int(input())
for i in range(m):
    a,b=input().split()
    if a=='update':
        list1 |=set(map(int,input().split()))
    elif a=='intersection_update':
        list1  &=set(map(int,input().split()))
    elif a=='difference_update':
        list1 -=set(map(int,input().split()))
    elif a=='symmetric_difference_update':
        list1 ^=set(map(int,input().split()))
print(sum(list1))

