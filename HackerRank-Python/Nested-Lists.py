if __name__ == '__main__':
    N = int(input())

    record = []

    if (2 <= N <= 5):
        for i in range(N):
            name = input()
            score = float(input())
            record.append([name, score])
        
        record.sort(key=lambda record: record[1])
        
        s_name = [] 
        s_score = []  
        
        for i in range(N):
            s_name.append(record[i][0])
            s_score.append(record[i][1])
        
        idx = 0    
        min_score = min(s_score)
        min2_score = min_score
        for i in range(N):
            if s_score[i] != min_score:
                idx = i
                min2_score = s_score[i]
                break
        
        r_name = []
        for i in range(idx,N):
            if s_score[i] != min2_score:
                break
            
            r_name.append(s_name[i])
        
        r_name.sort()
        for i in r_name:
            print(i)    
    