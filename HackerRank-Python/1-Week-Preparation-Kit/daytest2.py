#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    smtotal = 0
    smtotal1 = 0
    for i in range(n):
        left_to_right = arr[i][i]
        smtotal += left_to_right
        right_to_left = arr[i][(n-1)-i]
        smtotal1 += right_to_left
        
    result1 = abs(smtotal - smtotal1)
    
    print(result1)
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # result = diagonalDifference(arr)
    diagonalDifference(arr)
    # fptr.write(str(result) + '\n')

    # fptr.close()
