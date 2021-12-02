
valid = 0

with open('input') as f:
    for line in f:
        policy, password = line.split(':')
        # !!! 冒号后面有空格
        password = password.strip()
        low_high, ch = policy.split()
        low, high = low_high.split('-')
        low, high = int(low), int(high)
        cnt = 0
        for i, p in enumerate(password):
            if i + 1 in [low, high] and p == ch:
                cnt += 1

        if cnt == 1:
            valid += 1

print('valid: ', valid)


'''
python3 valid.py
valid:  509
'''