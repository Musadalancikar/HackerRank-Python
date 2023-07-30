
M = int(input())

a = input().split()
a = list(map(int, a))

N = int(input())

b = input().split()
b = list(map(int, b))

a = set(a)
b = set(b)

x = a.difference(b)
y = b.difference(a)

uni = x.union(y)
uni = list(uni)

for i in sorted(uni):
    print(i)
