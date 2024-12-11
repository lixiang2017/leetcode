import os
from collections import Counter

ans = 0


with open(os.path.join(os.path.dirname(__file__), 'input'), encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        nums = list(map(int, line.split()))


def rule(x):
    if x == 0:
        return [1]
    
    c = len(str(x))
    if c % 2 == 0:
        s = str(x)
        return [int(s[: c // 2]), int(s[c // 2: ])]
    
    return [x * 2024]

def blink(arr):
    for x in arr:
        for r in rule(x):
            yield r

blink_times = 75
nums_cnt = Counter(nums)
for t in range(blink_times):
    next_cnt = Counter()
    for x, cnt in nums_cnt.items():
        for r in rule(x):
            next_cnt[r] += cnt
    nums_cnt = next_cnt
    # print(nums)
    print("count: ", t + 1, sum(nums_cnt.values()))

print('ans:', sum(nums_cnt.values())) # ans: 279903140844645