m=int(input())
list1=set(map(int,input().split()))
n=int(input())
list2=set(map(int,input().split()))
list3=(list1.difference(list2)).union(list2.difference(list1))
for i in sorted(list(list3)):
    print(i)
