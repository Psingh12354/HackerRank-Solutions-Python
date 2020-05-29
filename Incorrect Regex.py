import re
t=int(input())
for i in range(0,t):
    try:
        re.compile(input())
        print("True")
    except re.error:
        print("False")

