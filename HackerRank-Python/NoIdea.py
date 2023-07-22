
n, m = input().split()

A = input().split()

B = set(input().split())
C = set(input().split())

print(sum([(i in B) - (i in C) for i in A]))