def average(array):
    # your code goes here
    
    array = set(array)
    
    ave = sum(array) / len(array)
    
    return ave


n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)