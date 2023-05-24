def count_substring(string, sub_string):
    
    string_len = len(string)
    sub_string_len = len(sub_string)
    a = 0
    
    for i in range(string_len-sub_string_len+1):
        if (string[i:(i+sub_string_len)] == sub_string):
            a=a+1
    return a

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)