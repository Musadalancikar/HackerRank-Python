N = int(input())

name_and_price_list = [] 

for i in range(N):
    name_and_price = input().split()
    name_and_price_list.append(name_and_price)
    
price = []
for i in name_and_price_list:
    price.append(i[-1])
    

name_list = []

for i in name_and_price_list:
    name_list.append(" ".join(i[:-1]))
    

A = list(zip(name_list, price))
result_list = [list(tpl) for tpl in A]
B = []

for i in result_list:
    if i[0] not in B:
        B.append(i[0])
    elif i[0] in B:
        try:
            index = [item[0] for item in result_list].index(i[0])
            b = int(result_list[index][1]) + int(i[1])
            result_list[index][1] = b
            
        except ValueError:
            continue

sozluk = {}

for item in result_list:
    key = item[0]
    value = item[1]
    if key not in sozluk:
        sozluk[key] = value

for key, value in sozluk.items():
    print(key,value)







