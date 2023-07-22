# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

a = int(input())

b = input().split()

total = 0

for i in range(a):
    names = namedtuple('colmnname', b)
    MARKS, CLASS, NAME, ID = input().split()
    colmnname = names(MARKS, CLASS, NAME, ID)
    total += int(colmnname.MARKS)
    
print((total / a))