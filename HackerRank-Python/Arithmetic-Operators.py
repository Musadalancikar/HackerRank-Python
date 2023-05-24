if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    def summ(a,b):
        return a+b
        
    def difference(a,b):
        return a-b
        
    def product(a,b):
        return a*b


    if (1 <= a <= 10**10) and ( 1 <= b <= 10**10):
        print(summ(a,b))
        print(difference(a,b))
        print(product(a,b))
    else:
        print("Error")

else:
    print("Error")