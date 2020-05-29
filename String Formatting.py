//<-1st method->//

def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        print(' '.join(map(lambda x: x.rjust(width), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
 
 //<-2nd method->//
 
 def print_formatted(number):
    for i in range(1,number+1):
        print("{0: d} {0: o} {0: x} {0:b}".format(i))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
  
  //<-In this 2nd method i need little bit improvement->//
  
