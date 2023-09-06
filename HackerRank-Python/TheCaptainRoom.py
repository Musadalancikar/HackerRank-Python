from collections import Counter

K = int(input())
room_list = list(map(int, input().split()))

sayac = Counter(room_list)

for eleman, sayi in sayac.items():
    if sayi == 1:
        print(eleman)
        break