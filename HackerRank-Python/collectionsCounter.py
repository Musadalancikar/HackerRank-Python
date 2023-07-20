shoe_number = int(input())

all_shoe_number = input().split()
all_shoe_number_list = [int(i) for i in all_shoe_number]

customers = int(input())

x = []

for i in range(customers):
    y,z = input().split()
    x.append((y,z))

y = []
for i in x:
    if int(i[0]) in all_shoe_number_list:
        all_shoe_number_list.remove(int(i[0]))
        y.append(int(i[1]))

print(sum(y))
        
    
