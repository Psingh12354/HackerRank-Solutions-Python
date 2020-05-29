import re
n,m=map(int,input().split(' '))
a=[]
for i in range(n):
    a.append(input()[:m])
    s=''.join(''.join(k) for k in zip(*a))
result = re.sub(r'([a-zA-Z0-9])([^a-zA-Z0-9]+)(?=[a-zA-Z0-9])', r'\1 ', s)
print(result)
