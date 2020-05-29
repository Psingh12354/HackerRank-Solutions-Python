k=int(input())
list1=sorted(map(int,input().split(' ')))
for i in range(1,len(list1)):
    if i!=len(list1)-1:
        if list1[i]!=list1[i-1] and list1[i]!=list1[i+1]:
            print(list1[i])
            break
    else:
        print(list1[i])
