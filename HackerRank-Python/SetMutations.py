

n = int(input())
n_list = set(map(int, input().split()))
a = int(input())

for i in range(a):
    x,y = input().split()
    z = set(map(int, input().split()))
    y = int(y)
    
    if x == "intersection_update" :
        n_list.intersection_update(z)
    elif x == "update":
        n_list.update(z)
    elif x == "symmetric_difference_update":
        n_list.symmetric_difference_update(z)
    elif x == "difference_update":
        n_list.difference_update(z)
    else:
        n_list = n_list
            
if 0 < len(n_list) < 1000:
    print(sum(n_list))
else:
    print(0)
