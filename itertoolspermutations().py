from itertools import permutations
s=input().split()
for i in sorted(permutations(s[0],int(s[1]))):
    print(''.join(i))
