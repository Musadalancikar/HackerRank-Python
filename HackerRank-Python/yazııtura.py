import random

n = int(input())
liste = []
for i in range(n):
    randmmm = random.randint(0, 1)
    if randmmm == 0:
        liste.append("Yazı")
        
    elif randmmm == 1:
        liste.append("Tura")
        
    else:
        print("Dik geldi")
        

cnt = liste.count("Yazı")
cnt1 = liste.count("Tura")

if cnt > cnt1:
    print("yazı kazandı")
elif cnt < cnt1:
    print("tura kazandı")
    
else:
    print("Berabere")
    