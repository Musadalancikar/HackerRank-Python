if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    liste = list(set(arr))

    if -100 <= len(liste) <= 100:
        if (2 <= n <= 10):
            max_number = max(liste)
            liste.remove(max_number)
            second_max_number = max(liste)
            print(second_max_number)
        else:
            print("Error")                  
    else: 
        print("Error")        