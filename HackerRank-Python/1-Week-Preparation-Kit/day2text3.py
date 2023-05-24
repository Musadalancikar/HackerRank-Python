#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    # Write your code here
    a = max(arr)

    if n <= 100:
        result = [0] * n
        for number in arr:
            result[number] += 1
        print(result)
    else:
        result = [0] * int(a+1)
        for number in arr:
            result[number] += 1
        print(result)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
