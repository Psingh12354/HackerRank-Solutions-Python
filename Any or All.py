n=int(input())
list1=list(map(int,input().split(' ')))
print(all(i>0 for i in list1) and any(str(i)==str(i)[::-1] for i in list1))
