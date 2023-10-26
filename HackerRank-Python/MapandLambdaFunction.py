cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    listt = [0, 1]
    if n > 1:    
        for i in range(1, n-1):
            listt.append(listt[i-1]+listt[i])
        return listt
    else:
        return listt[:n]
    

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))