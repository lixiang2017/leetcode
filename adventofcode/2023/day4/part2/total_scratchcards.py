import os 

path = os.path.join(os.path.dirname(__file__), "input")



match_count = []
with open(path) as f:
    for line in f:
        card, numbers = line.strip().split(":")
        winning, have = numbers.strip().split("|")
        winning_numbers = set(winning.strip().split())
        count = sum(x in winning_numbers for x in have.strip().split())
        match_count.append(count)


cards = [1] * len(match_count)
for i, m in enumerate(match_count):
    for j in range(1, m + 1):
        if i + j < len(match_count):
            cards[i + j] += cards[i]
        else:
            break 
print('ans ', sum(cards)) # 30 # 8172507