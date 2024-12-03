import os 
from itertools import pairwise

ans = 0

def is_safe(a):
    b = sorted(a)
    c = sorted(a, reverse=True)
    if not (a == b or a == c):
        return False 
    return all(1 <= abs(x - y) <= 3 for x, y in pairwise(a))

with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
    for line in f:
        a = list(map(int, line.split()))
        ans += int(is_safe(a))

print('ans: ', ans) # ans:  502