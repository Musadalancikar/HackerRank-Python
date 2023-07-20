def minion_game(string):
    # your code goes here
        
    a = 0
    b = 0
    
    vowel = 'AEIOU'
    
    for i in range(len(string)):
        if string[i] not in vowel:
            a = a + (len(s)-i)
        
        else:
            b = b + (len(s)-i)
            
    if a > b:
        print("Stuart", a)
        
    elif b > a:
        print("Kevin", b)
        
    else:
        print("Draw")


s = input()
print(minion_game(s))
