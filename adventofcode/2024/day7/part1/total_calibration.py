import os 

ans = 0

def predict(line):
    left, right = line.split(":")
    test_value = int(left)
    nums = list(map(int, right.strip().split(" ")))
    possible = {nums.pop(0)}
    for nxt in nums:
        possible = {p * nxt for p in possible} | {p + nxt for p in possible}
        
    if test_value in possible:
        return test_value
    else:
        return 0

with open(os.path.join(os.path.dirname(__file__), 'input'), encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        ans += predict(line)

print('ans: ', ans) # ans:  3598800864292