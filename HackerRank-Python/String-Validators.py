if __name__ == '__main__':
    s = input()
    
    def isaln(s): 
        a = 0
        for i in s:
            if i.isalnum() == True:
                a += 1
            else:
                a = a
        if a >= 1:
            return True
        else:
            return False
  
    def isalp(s):
        b = 0
        for i in s:
            if i.isalpha() == True:
                b += 1
            else:
                b = b
        if b >= 1:
            return True
        else:
            return False
    def isdi(s):
        c = 0
        for i in s:
            if i.isdigit() == True:
                c += 1
            else:
                c = c
                
        if c >= 1:
            return True
        else:
            return False
        
    def islo(s):
        d = 0
        for i in s:
            if i.islower() == True:
                d += 1
            else:
                d = d
                
        if d >= 1:
            return True
        else:
            return False
        
    def isup(s):
        e = 0
        for i in s:
            if i.isupper() == True:
                e += 1
            else:
                e = e
                
        if e >= 1:
            return True
        else:
            return False
    
    
        
    f = isaln(s)
    print(f)
    g = isalp(s)
    print(g)
    h = isdi(s)
    print(h)
    k = islo(s)
    print(k)
    l = isup(s)
    print(l)
    
    
    