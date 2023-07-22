import math

def degre(x1, x2):
    maths = x1 / x2
        
    return round(math.degrees(math.atan(maths)))
    
x1 = int(input())
x2 = int(input())

a = degre(x1, x2)

print(str(a)+"\u00b0")