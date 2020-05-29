from collections import OrderedDict
n=int(input())
order = OrderedDict()
for i in range(n):
    name, space, price = input().rpartition(' ')
    order[name] = order.get(name, 0) + int(price)
for name, price in order.items():
    print(name, price)
