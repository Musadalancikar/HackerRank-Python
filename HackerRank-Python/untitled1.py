

T = int(input())

list_all = []
for i in range(T):
    size = int(input())
    blocks = list(map(int, input().split()))
    if size == len(blocks):
        list_all.append(blocks)
    else:
        print("size != len(blocks)")

sayac = 0
for a in range(T):
    for i in range(len(list_all[a])-1):
        if list_all[a][0] < list_all[a][i+1]:
            print("No")
            break
        else:
            sayac += 1
        
        if sayac == (len(list_all[a])-1):
            print("Yes")


