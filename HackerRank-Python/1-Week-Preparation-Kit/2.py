#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_number = min(arr)
    max_number = max(arr)
    
    copy_arr = arr.copy()
    
    copy_arr.remove(min_number)
    sum_max = sum(copy_arr)
        
    copy_arr1 = arr.copy()
    
    copy_arr1.remove(max_number)
    sum_min = sum(copy_arr1) 
    
    print(sum_min, sum_max)
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
