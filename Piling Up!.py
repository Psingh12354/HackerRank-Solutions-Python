from collections import deque
t=int(input())
for i in range(t):
    flag=True
    input()
    a=deque(map(int,input().split()))
    if(a[0]>=a[-1]):
        max=a.popleft()
    else:
        max=a.pop()
    while a:
        if len(a)==1:
            if(a[0]<=max):
                break
            else:
                flag=False
                break;
        else:
            if a[0]<max and a[-1]<=max:
                if a[0]>=a[-1]:
                    max=a.popleft()
                else:
                    max=a.pop()
            elif a[0]<=max:
                max=a.popleft()
            elif a[-1]<=max:
                max=a.pop()
            else:
                flag=False
                break;
    if flag:
        print('Yes')
    else:
        print('No')



