

from itertools import product


x = input().split()
a = [int(i) for i in x]
y = input().split()
b = [int(i) for i in y]

print(*product(a,b))




