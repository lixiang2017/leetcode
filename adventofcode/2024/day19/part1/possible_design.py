from pathlib import Path
import os
import re

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")
towels, designs = re.split("\n\n", lines)

towels = set(map(str.strip, towels.split(",")))
designs = re.split("\n", designs)
print("towels ", towels)
# print("designs ", designs)

def is_possible0(design, index, L):
    # print(design, index, L)
    if index == L:
        return True
    for towel in towels:
        # print("towel ", towel)
        if index + len(towel) > L:
            continue
        # print(" part ", design[index: index + len(towel)])
        if towel == design[index: index + len(towel)]:
            if is_possible(design, index + len(towel), L):
                return True
    return False

def is_possible(design, depth):
    print("design " , design, depth)
    if len(design) == 0 or design in towels:
        print("True")
        return True
    if len(design) == 1 and design not in towels:
        print("False")
        return False
    for towel in towels:
        if design.startswith(towel):
            if is_possible(design[len(towel): ], depth + 1):
                return True
    return False

design = ["uwrbubuwrwgbubguguurwwurbrurbwbwwwgbrwwwg"]
print("g" in towels)

for design in designs:
    design = design.strip()
    print('testing ', design)
    # if is_possible(design, 0, len(design)):
    if is_possible(design, 0):
        ans += 1
print('ans:', ans)