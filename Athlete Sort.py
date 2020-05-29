n,m=map(eval,input().split())
elements=[input() for i in range(n)]
k=eval(input())
for element in sorted(elements,key=lambda element: eval(element.split()[k])):
    print(element)
