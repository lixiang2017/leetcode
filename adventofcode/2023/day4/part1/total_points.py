import os 

path = os.path.join(os.path.dirname(__file__), "input")

ans = 0
with open(path) as f:
    for line in f:
        card, numbers = line.strip().split(":")
        winning, have = numbers.strip().split("|")
        winning_numbers = set(winning.strip().split())
        count = sum(x in winning_numbers for x in have.strip().split())
        if count > 0:
            ans += pow(2, count - 1)

print('ans ', ans) # 13