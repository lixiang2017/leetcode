import os 

ans = 0

memo = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
# 3, 4, 5


def get_first_last_digit(line):
    digits = []
    for i, ch in enumerate(line):
        if ch.isdigit():
            digits.append(int(ch))
        else:
            for length in [3, 4, 5]:
                if line[i: i + length] in memo:
                    digits.append(memo.get(line[i: i + length]))
    a, b = digits[0], digits[-1]
    return a, b


with open(os.path.join(os.path.dirname(__file__), 'input')) as f:
    for line in f:
        a, b = get_first_last_digit(line)
        ans += 10 * a + b 

print('ans: ', ans) # ans:  281   56017