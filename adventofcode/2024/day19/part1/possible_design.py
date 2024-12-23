from pathlib import Path
import os
import re
from functools import cache


ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")
towels, designs = re.split("\n\n", lines)

towels = set(map(str.strip, towels.split(",")))
designs = re.split("\n", designs)
print("towels ", towels)
# print("designs ", designs)


# should use memoization, otherwise will be endless running
memo = {}
def is_possible0(design):
    if design in memo:
        return memo[design]
    if 0 == len(design):
        memo[design] = True
        return True
    for towel in towels:
        if len(towel) > len(design):
            continue
        if towel == design[: len(towel)]:
            if is_possible0(design[len(towel): ]):
                memo[design] = True
                return True

    memo[design] = False
    return False

@cache
def is_possible1(design):
    if len(design) == 0 or design in towels:
        return True
    for towel in towels:
        if design.startswith(towel):
            if is_possible1(design[len(towel): ]):
                return True
    return False


for design in designs:
    design = design.strip()
    print('testing ', design)
    # good
    if is_possible0(design):
    ## also good
    # if is_possible1(design):
        ans += 1
print('ans:', ans) # ans: 365