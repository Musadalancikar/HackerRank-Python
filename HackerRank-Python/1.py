
N = int(input())

list_name = []
for i in range(N):
    list_name.append(input())
    
c = []
for i in list_name:
    if i not in c:
        c.append(i)

d = []
for i in c:
    d.append(list_name.count(i))
    
print(len(set(list_name)))
print(*d)

