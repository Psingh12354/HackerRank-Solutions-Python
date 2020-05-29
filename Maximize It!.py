import itertools
k, m = map(int, input().split(' '))
arr = []
for i in range(k):
    arr.append(input().split(' ')[1:])
maxi = 0
for j in itertools.product(*arr):
    result = sum([int(x)**2 for x in j]) % m
    if result > maxi:
        maxi = result
print(maxi)
