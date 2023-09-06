from itertools import product

N,M = map(int, input().split())

l=[]

for i in range(N):
    x = list(map(int,input().split()))[1:]
    l.append(x)

s = map(lambda x:sum(i*i for i in x)%M,product(*l))
print(max(s))