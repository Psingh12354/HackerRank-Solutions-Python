s=input()
print(*sorted(s, key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')
