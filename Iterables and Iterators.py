from itertools import combinations
n=int(input())
letter=input().split(' ')
k=int(input())
count,total=0,0
for i in combinations(letter,k):
    count+='a' in i
    total+=1
print(count/total)
