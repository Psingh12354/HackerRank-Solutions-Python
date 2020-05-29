from collections import OrderedDict
n=int(input())
word=OrderedDict()
for i in range(0,n):
    k=input()
    if k in word:
        word[k]+=1
    else:
        word[k]=1
print(len(word))
print(' '.join(map(str,word.values())))
