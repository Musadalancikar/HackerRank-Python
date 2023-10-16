def subset(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set2.issubset(set1)

setA = list(map(int, input().split()))

N = int(input())

a = []
for i in range(N):
    setB = list(map(int, input().split()))
    a.append(subset(setA, setB))
    
if False in a:
    print("False")
else:
    print("True")