
n = int(input())

for i in range(1,n+1):
    if i == 1:
        print(str(i).ljust(i))
    else:
        print(str(i-1).ljust(i-i)+str(i).center(i-i)+str(i-1).ljust(i-i))