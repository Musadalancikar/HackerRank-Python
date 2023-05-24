
x, y = map(int,input().split())

s1 = '.|.'
s2 = 'WELCOME'

for i in range(x//2):
    print((s1*((i*2)+1)).center(y,'-'))
    
print(s2.center(y,'-'))

a = x // 2
b = (2*a)-1

for i in range(x//2):
    print((s1*((i*(-2))+b)).center(y,'-'))
    

    