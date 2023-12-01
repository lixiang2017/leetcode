import os 

ans = 0

def get_first_last_digit(line):
    digits = list(map(int, filter(str.isdigit, line)))
    a, b = digits[0], digits[-1]
    return a, b


with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
    for line in f:
        a, b = get_first_last_digit(line)
        ans += 10 * a + b 

print('ans: ', ans) # ans:  56506