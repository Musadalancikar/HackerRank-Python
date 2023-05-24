n = input()
t = []
a = input().split()
for i in a:
    if len(a) == int(n):    
        t.append(int(i))
        
    else:
        break

def convert(list):
    return tuple(list)

t = convert(t)

print(hash(t))



