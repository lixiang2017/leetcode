import os 
from itertools import pairwise

input_path_from_part1 = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'part1'), 'input')

ans = 0

def is_safe(a):
    b = sorted(a)
    c = sorted(a, reverse=True)
    if not (a == b or a == c):
        return False 
    return all(1 <= abs(x - y) <= 3 for x, y in pairwise(a))

with open(input_path_from_part1) as f:
    for line in f:
        a = list(map(int, line.split()))
        if is_safe(a):
            ans += 1
        else:
            for i in range(len(a)):
                removed_a = a[: i] + a[i + 1: ]
                if is_safe(removed_a):
                    ans += 1
                    break 

print('ans: ', ans) # ans:  544