

x, y = list(map(int, input().split()))

groupA = []
for i in range(x):
    a = input()
    groupA.append(a)

print(groupA)

groupB = []
for i in range(y):
    b = input()
    groupB.append(b)

print(groupB)


s = []
for i in groupA:
    if i in groupB:
        s.append(groupA.index(i))
       

