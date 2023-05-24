if __name__ == '__main__':
    N = int(input())
    list = []
    
    for i in range(N):
        message = input().split()
        
        if message[0] == 'print':
            print(list)
        
        elif message[0] == 'append':
            list.append(int(message[1]))
            
        elif message[0] == 'sort':
            list.sort()
        
        elif message[0] == 'insert':
            list.insert(int(message[1]),int(message[2]))
            
        elif message[0] == 'remove':
            list.remove(message[1])
            
        elif message[0] == 'pop':
            list.pop()
            
        elif message[0] == 'reverse':
            list.reverse()
            
        
        else:
            print("No")
            