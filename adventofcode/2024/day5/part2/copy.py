# copy from https://www.reddit.com/r/adventofcode/comments/1h71eyz/2024_day_5_solutions/
# cat /home/lixiang/leetcode/adventofcode/2024/day5/part1/input | python /home/lixiang/leetcode/adventofcode/2024/day5/part2/copy.py

import sys
from functools import cmp_to_key

def parse_rules(f):
    rules = {}
    for line in f:
        if line == '\n':
            break
        left, right = map(int, line.split('|'))
        rules.setdefault(right, set()).add(left)
        rules.setdefault(left, set())
    return rules

def order(update, rules):
    def compare(a, b):
        return -1 if a in rules[b] else b in rules[a]
    return tuple(sorted(update, key=cmp_to_key(compare)))

rules = parse_rules(sys.stdin)
updates = [tuple(map(int, line.split(','))) for line in sys.stdin]
ordered = [order(update, rules) for update in updates]
print(sum(u[len(u) // 2] for u, o in zip(updates, ordered) if u == o))
print(sum(o[len(o) // 2] for u, o in zip(updates, ordered) if u != o))
# 7307
# 4713
