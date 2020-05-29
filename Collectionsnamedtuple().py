from collections import namedtuple
n=int(input())
X=input().split()
Tot_Marks=0
for i in range(n):
    A=namedtuple('A',X)
    MARKS,CLASS,NAME,ID=input().split()
    A=A(MARKS,CLASS,NAME,ID)
    Tot_Marks+=int(A.MARKS)
print('{:.2f}'.format(Tot_Marks/n))
