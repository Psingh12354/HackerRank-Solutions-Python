cube = lambda x: x**3
def fibonacci(n):
    lis=[]
    for i in range(n):
        if i<2:
            lis+=[i]
        else:
            lis+=[lis[-1]+lis[-2]]
    return lis
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
