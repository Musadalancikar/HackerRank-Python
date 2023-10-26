n = int(input())

def flo(f):
    try:
        if ((f[0] == "+" and f[1] != "+") and (f[0] == "+" and f[1] != "-")) or ((f[0] == "-" and f[1] != "+") and (f[0] == "-" and f[1] != "-")):
            if float("".join(f[1:])):
                return True
            else:
                return False
        elif float("".join(f)):
            return True
        else:
            return False
    except ValueError:
        return False
        
total = []
        
for i in range(n):
    f = list(input())
    total.append(flo(f))

for j in total:
    print(j)