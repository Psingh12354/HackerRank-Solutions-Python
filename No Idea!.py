n,m=([int(i) for i in input().split(' ')])
arr=map(int,input().split(' '))
a=set(map(int,input().split(' ')))
b=set(map(int,input().split(' ')))
result=0
for i in arr:
    if i in a:
        result+=1
    if i in b:
        result+=-1
print(result)
