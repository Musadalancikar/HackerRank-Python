#!/bin/python3

import math
import os
import random
import re
import sys

def sorted_index(arr, k):
    total = []
    for i in range(len(arr)):
        total.append(arr[i][k])
    total = sorted(total)
    total_result = []
    for j in total:
        for l in range(len(arr)):
            if arr[l][k] == j:
                total_result.append(arr[l])
                arr.remove(arr[l])
                break
    return total_result

if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    total_result = sorted_index(arr,k)
    for i in total_result:
        print(*i)
