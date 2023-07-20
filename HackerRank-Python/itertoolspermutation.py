from itertools import permutations


x, y = input().split()

x = list(x)
y = int(y)

a = list(permutations(x,y))

b = []
for i in a:
    z = "".join(i)
    b.append(z)

sort_list = sorted(b)

for i in sort_list:
    print(i)