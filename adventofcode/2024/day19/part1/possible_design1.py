from pathlib import Path
import os
import re
from collections import defaultdict
from functools import cache

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")
towels, designs = re.split("\n\n", lines)

towels = list(map(str.strip, towels.split(",")))
designs = re.split("\n", designs)
# print("towels ", towels)
# print("designs ", designs)


Trie = lambda: defaultdict(Trie)
t = Trie()

for towel in towels:
    tt = t
    cnt = 0
    for ch in towel:
        tt = tt[ch]
        cnt += 1
    tt["#"] = cnt

# should use memoization
@cache
def is_possible(design, index, L):
    if index == L:
        return True
    tt = t
    # index, could try
    end_indice = []
    while index < L and design[index] in tt:
        tt = tt[design[index]]
        index += 1
        if "#" in tt:
            end_indice.append(index)
    for i in reversed(end_indice):
        if is_possible(design, i, L):
            return True
    return False


for design in designs:
    if is_possible(design, 0, len(design)):
        ans += 1
print('ans:', ans) # ans: 365