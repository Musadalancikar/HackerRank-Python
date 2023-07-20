def print_rangoli(size):
    # your code goes here
    alf = "abcdefghijklmnopqrstuvwxyz"
    
    alf_list = [alf[i] for i in range(size)]
    
    size_list = list(range(size))
    size_list = size_list[:-1]+size_list[::-1]
    
    for i in size_list:
        a = alf_list[-(i+1):]
        b = a[::-1]+a[1:]
        print("-".join(b).center(((4*n)-3), "-"))

    

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
