import cmath

def abss(x):
    return abs(x)

def phasee(x):
    return cmath.phase(x)

# print(abs(x))
# print(cmath.phase(x))

x = complex(input())
print(abss(x))
print(phasee(x))
