import os 

ans = 0

def concatenate(p, nxt):
    return int(str(p) + str(nxt))

def predict(line):
    left, right = line.split(":")
    test_value = int(left)
    nums = list(map(int, right.strip().split(" ")))
    possible = {nums.pop(0)}
    for nxt in nums:
        possible = {p * nxt for p in possible} | {p + nxt for p in possible} | {concatenate(p, nxt) for p in possible}
        
    if test_value in possible:
        return test_value
    else:
        return 0

input_path_from_part1 = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'part1'), 'input')
with open(input_path_from_part1, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        ans += predict(line)
 
print('ans: ', ans) # ans:  340362529351427