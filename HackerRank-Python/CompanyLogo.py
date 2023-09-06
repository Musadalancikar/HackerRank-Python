import math
import os
import random
import re
import sys
from collections import Counter

if __name__ == '__main__':
    
    s = input()
    s = sorted(s)
    
    fre = Counter(list(s))
    
    for a, b in fre.most_common(3):
        print(a, b)
    








