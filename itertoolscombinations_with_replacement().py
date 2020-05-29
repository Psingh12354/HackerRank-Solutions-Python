from itertools import combinations_with_replacement
s=input().split()
for i in combinations_with_replacement(sorted(s[0]),int(s[1])):
    print(''.join(i))
