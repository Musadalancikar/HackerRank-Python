from itertools import combinations_with_replacement

x, y = input().split()

x = sorted(list(x))
y = int(y)

a = list(combinations_with_replacement(x, y))

for i in a:
    print("".join(i))