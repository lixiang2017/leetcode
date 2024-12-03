import os 
from collections import Counter

ans = 0
array_a, array_b = [], []

input_path_from_part1 = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'part1'), 'input')
with open(input_path_from_part1) as f:
    for line in f:
        a, b = list(map(int, line.split()))
        array_a.append(a)
        array_b.append(b)

c1, c2 = Counter(array_a), Counter(array_b)
for x, c in c1.items():
    ans += c * x * c2[x]
print('ans: ', ans) # ans:  24869388