#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def plusMinus(arr):
    # Write your code here
    pst_number = 0
    zero_number = 0
    neg_number = 0
    for i in arr:
        if i > 0:
            pst_number += 1 
        elif i == 0:
            zero_number += 1
            
        elif i < 0:
            neg_number += 1
    
    postive_number_ratios = round(pst_number/len(arr),6)
    negative_number_ratios = round(neg_number/len(arr),6)
    zero_number_ratios = round(zero_number/len(arr), 6)
    
    print(postive_number_ratios)
    print(negative_number_ratios)
    print(zero_number_ratios)
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

