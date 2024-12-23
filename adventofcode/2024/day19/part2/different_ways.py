# https://github.com/scorixear/AdventOfCode/blob/main/2024/19/2.py
from pathlib import Path
import os
import re
from functools import cache
from collections import Counter

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")
towels, designs = re.split("\n\n", lines)

towels = set(map(str.strip, towels.split(",")))
designs = re.split("\n", designs)
# print("towels ", towels)
# print("designs ", designs)


def find_path(towels: list[str], design: str, dp: dict[str, int]) -> int:
    if len(design) == 0:
        return 1
    if design in dp:
        return dp[design]
    total = 0
    for towel in towels:
        if design.startswith(towel):
            total += find_path(towels, design[len(towel):], dp)
    dp[design] = total
    return total

dp = {}
for design in designs:
    w = find_path(towels, design, dp)
    ans += w
print('ans:', ans) # ans: 730121486795169