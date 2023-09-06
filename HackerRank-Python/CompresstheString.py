
from itertools import groupby

a = []
def groupbyy(iterable, keyfunc=None):
    for k, g in groupby(iterable, keyfunc):
        a.append((len(list(g)),int(k)))
        
        
groupbyy(input())

print(*a)
