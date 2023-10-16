x, k = list(map(int, input().split()))

polynom = input().split(" ")

total = 0

for i in range(len(polynom)):
    if "x**" in polynom[i]:
        b = list(polynom[i])
        if b[0] == "x":
            try:
                if polynom[i-1] == "-":
                    a = list(polynom[i])
                    total -= (x** int(a[-1]))
                else:
                    a = list(polynom[i])
                    total += (x** int(a[-1]))
            except:
                continue
        else:
            try:
                if polynom[i-1] == "-":
                    a = list(polynom[i])
                    total -= int(a[0]) * (x** int(a[-1]))
                else:
                    a = list(polynom[i])
                    total += int(a[0]) * (x** int(a[-1]))
            except:
                continue
        
    elif polynom[i] == "x":
        if polynom[i-1] == "-":
            total -= (x** 1)
        else:
            total += (x** 1)
        
    elif polynom[i] == "-" or polynom[i] == "+":
        total = total

    else:
        if polynom[i-1] == "-":
            total -= int(polynom[i])
        else:
            total += int(polynom[i])
        
if total == k:
    print("True")
    
else:
    print("False")
     
            
        
                




