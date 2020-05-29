import re
n=int(input())
for i in range(n):
    s = input().strip()
    pre = re.search(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$',s)
    if pre:
        processed= "".join(pre.group(0).split('-'))
        final = re.search(r'(\d)\1{3,}',processed)
        print ('Invalid' if final else 'Valid')
    else:
        print('Invalid')
