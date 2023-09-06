import re

N = int(input())

def is_valid_regex(regex_str):
    try:
        re.compile(regex_str)
        return True
    except re.error:
        return False
    
a = []

for i in range(N):
    a.append(is_valid_regex(input()))
    
for i in a:
    print(i)
