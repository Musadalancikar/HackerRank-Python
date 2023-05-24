#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr.sort()
    # print(arr)
    if (n % 2) == 1:
        islem = n // 2
        print(arr[islem])
    else:
        i = n // 2
        print((arr[i-1] + arr[i]) / 2)
    
    
if __name__ == '__main__':
    n = int(input().strip())
    
    arr = list(map(int, input().rstrip().split()))
    
    findMedian(arr)

