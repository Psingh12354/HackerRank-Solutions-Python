a=set(map(int,input().split(' ')))
isstrictsuperset = True
for i in range(int(input())):
    set1=set(map(int,input().split()))
    if not set1.issubset(a):
        isstrictsuperset=False
    if len(set1)>=len(a):
        isstrictsuperset=False
print(isstrictsuperset)
