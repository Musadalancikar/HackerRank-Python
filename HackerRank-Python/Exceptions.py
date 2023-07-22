
n = int(input())

a = []
for i in range(n):
    x, y = input().split()
    a.append((x,y))


for i in a:
    try:
        islem = int(i[0]) / int(i[1])
        print(int(islem))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
        
    except ValueError as c:
        print("Error Code:", c)
        

