

valid = 0

with open('input') as f:
    for line in f:
        policy, password = line.split(':')
        low_high, ch = policy.split()
        low, high = low_high.split('-')
        low, high = int(low), int(high)
        cnt = 0
        for p in password:
            if p == ch:
                cnt += 1
        if low <= cnt <= high:
            valid += 1

print('valid: ', valid)

'''
python3 valid.py
valid:  434
'''