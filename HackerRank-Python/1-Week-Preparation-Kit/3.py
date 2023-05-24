#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here

    meridiem = s[-2:]
    saat = s[:-2].split(':')


    saat[0] = int(saat[0])


    if meridiem == "PM" and saat[0] != 12:
        saat[0] += 12


    if meridiem == "AM" and saat[0] == 12:
        saat[0] -= 12


    saat24 = "{:02d}:{:02d}:{:02d}".format(saat[0], int(saat[1]), int(saat[2]))

    return saat24

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

