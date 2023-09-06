A = int(input())
a_list = set(map(int, input().split()))

B = int(input())
b_list = set(map(int, input().split()))

print(len(a_list.difference(b_list)))