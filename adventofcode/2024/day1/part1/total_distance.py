import os 

ans = 0
array_a, array_b = [], []

with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
    for line in f:
        a, b = list(map(int, line.split()))
        array_a.append(a)
        array_b.append(b)

array_a.sort()
array_b.sort()

ans = sum(abs(a - b) for a, b in zip(array_a, array_b))
print('ans: ', ans) # ans:  1110981