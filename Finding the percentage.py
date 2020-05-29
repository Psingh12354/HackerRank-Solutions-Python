n=int(input())
Marks={}
for i in range(0,n):
    A=input().split()
    marks=list(map(float,A[1:]))
    Marks[A[0]]=sum(marks)/float(len(marks))
print( "%.2f" % Marks[input()] )

