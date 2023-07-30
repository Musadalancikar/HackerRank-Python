from itertools import product

x = int(input())
y = int(input())
z = int(input())
n = int(input())


i = [a for a in range(0,x+1)]
j = [b for b in range(0,y+1)]
k = [c for c in range(0,z+1)]

perm_list = list(product(i, j, k))

perm_list1 = []

for perm in perm_list:
    perm_list1.append(list(perm))
    
perm_list2 = []

for i in perm_list1:
    if sum(i) != n:
        perm_list2.append(i)
    else:
        continue
    
print(perm_list2)