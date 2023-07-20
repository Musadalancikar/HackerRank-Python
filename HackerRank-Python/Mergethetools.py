
def merge_the_tools(string, k):
    # your code goes here

    a = len(string)
    
    b = int(a / k)

    c = []
    
    for i in range(b):       
        x = string[(k*i):(k*(i+1))]
        # x = list(set(x))
        c.append(x)        
    
    for i in c:
        kelime_listesi = []
        sonuc = ""
        for harf in i:
            if harf not in kelime_listesi:
                kelime_listesi.append(harf)
                sonuc += harf
            
        print(sonuc)
    
string, k = input(), int(input())
merge_the_tools(string, k)