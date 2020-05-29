import re
n=int(input())
r=re.compile("^[789]\d{9}$")
for i in range(n):
    number=input()
    if r.search(number):
        print("YES")
    else:
        print("NO")
