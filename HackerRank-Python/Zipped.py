
n, x = list(map(int, input().split()))

zip_list = []

for i in range(x):
    zip_list.append(list(map(float, input().split())))
        
result = zip(*zip_list)
result = list(result)

for j in result:
    print(sum(j)/x)

