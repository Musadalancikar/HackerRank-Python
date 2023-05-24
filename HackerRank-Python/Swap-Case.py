def swap_case(s):
    t = []

    for i in s:
        if isinstance(i, str):
            if i.isupper():
                i = i.lower()
                t.append(i)
            elif i.islower():
                i = i.upper()
                t.append(i)
            else:
                t.append(i)
        else:
            t.append(i)
    
    yenistring = ''.join(t)
    return yenistring
        
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
