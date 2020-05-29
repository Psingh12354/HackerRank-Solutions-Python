from collections import deque
n=int(input())
d=deque()
for i in range(n):
    s=input().strip().split()
    if (s[0]=="append"):
        d.append(s[1])
    elif (s[0]=="pop"):
        d.pop()
    elif (s[0]=="popleft"):
        d.popleft()
    elif (s[0]=="appendleft"):
        d.appendleft(s[1])
print(' '.join(d))
