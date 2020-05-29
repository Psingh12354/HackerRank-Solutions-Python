import re
m=input()
s=re.search(r"(?P<repeat>([a-z0-9])\2?(?:\2))+",m)
print(s.groupdict()['repeat'][0] if s else '-1')

