n = int(input())
numbr_list = list(map(int, input().split()))

def all_any(numbr_list):
    if len(numbr_list) > 3:
        total = 0
        for i in numbr_list:
            if all([i > 0]) == True:
                total += 1    
        if total == len(numbr_list):
            return True
        else:
            return False
    else:
        return False
        
print(all_any(numbr_list))