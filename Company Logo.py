from collections import Counter
for i,counts in sorted(Counter(input()).most_common(),key=lambda x:(-x[1],x[0]))[:3]:
    print(i,counts)
