
s = list(input())

def strng(s):
    upper_list = []
    lower_list = []
    even_list = []
    odd_list = []
    for i in s:
        if i.isupper() == True:
            upper_list.append(i)
        elif i.islower() == True:
            lower_list.append(i)
        elif int(i) % 2 == 0:
            even_list.append(i)
        elif int(i) % 2 == 1:
            odd_list.append(i)
    
    upper_list = sorted(upper_list)
    lower_list = sorted(lower_list)
    even_list = sorted(even_list)
    odd_list = sorted(odd_list)
    
    total =  lower_list + upper_list + odd_list + even_list
    return "".join(total)

print(strng(s))
    