
T = int(input())

def subset(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.issubset(set2)

for i in range(T):
    A = int(input())
    lstA = list(map(int, input().split()))
    B = int(input())
    lstB = list(map(int, input().split()))
    print(subset(lstA, lstB))
      