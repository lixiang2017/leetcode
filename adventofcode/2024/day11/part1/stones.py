import os

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

blink_times = 25
for t in range(blink_times):
    b = blink(nums)
    nums = list(b)
    # print(nums)
    print("count: ", t + 1, len(nums))

print('ans:', len(nums)) # ans: 235850