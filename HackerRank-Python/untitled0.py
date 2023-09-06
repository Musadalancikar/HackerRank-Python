
import math
import os
import random
import re
import sys

s = input()

from itertools import groupby

a = []
def groupbyy(iterable, keyfunc=None):
    for k, g in groupby(iterable, keyfunc):
        a.append([len(list(g)),k])
        
groupbyy(s)

# print(*a)

b = []
for i in range(len(a)):
    b.append(a[i][0])

d = b.copy()
for i in range(3):
    c = b.index(max(d))
    d.remove(max(d))
    print(f"{a[c][1]} {a[c][0]}")
    