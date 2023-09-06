kardiz = "İstanbul Büyükşehir Belediyesi"

a = kardiz.split()

b = []
for i in a:
    b.append(i[0])
    
print("".join(b))