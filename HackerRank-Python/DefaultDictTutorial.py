from collections import defaultdict

x, y = map(int, input().split())

d = defaultdict(list)

for i in range(x):
    d[input()].append(i+1)
for j in range(y):
    s = input()
    if s in d:
        print(*d[s])
    else:
        print(-1)