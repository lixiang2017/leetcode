from pathlib import Path
import os
import re
from collections import defaultdict

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")
towels, designs = re.split("\n\n", lines)

towels = list(map(str.strip, towels.split(",")))
designs = re.split("\n", designs)
print("towels ", towels)
min_len = min(len(t) for t in towels)
max_len = max(len(t) for t in towels)
print("min max len ", min_len, max_len) # min max len  1 8
print("designs ", designs)


Trie = lambda: defaultdict(Trie)
t = Trie()

for towel in towels:
    tt = t
    cnt = 0
    for ch in towel:
        tt = tt[ch]
        cnt += 1
    tt["#"] = cnt

def is_possible(design, index, L, t):
    # print(design, index, L)
    if index == L:
        return True
    possible = False
    tt = t
    # index, could try
    end_indice = []
    while index < L and design[index] in tt:
        tt = tt[design[index]]
        index += 1
        if "#" in tt:
            end_indice.append(index)
    for i in reversed(end_indice):
        possible |= is_possible(design, i, L, t)
        if possible:
            return True
    return possible


# designs = []
# special = ["uwrbubuwrwgbubguguurwwurbrurbwbwwwgbrwwwg", 
#            "rwbuwurwurgrrurbbgwbrgwguwwbrbbwgbbwwugbuuwwubuuwwg", 
#            "ubbgwuwwubggrguuwbrwbrwrrrurugrrbubrgubgbrwwg", "bgbuubuggburgwrbrbwwrwrguubbrwugubbuwbrgrwwugbgwggbrbrbuwwg",
#            "bwbwubbrugwbbggwugbrrwrrwwwwwgbbgrrwurrgrbrgwbwrbbwuurgwwwg",
#            "wuwgwwguwbbrbbrwuwwburruguwuubbruuwrurrwwuurrrwwgbwg",
#            "rrgurruwbbubgwbgruwwrrgwuruggbbgwwrubuwwggwg",
#            "wgubwwuwwwrbgbgwgrwugubgrwbrbruwwgbubbuuwwg",
#            "wbbgrrwwbgrubggggwuuurburuwbguuggwugbwgrrgwwg"]

for design in designs:
    print('testing ', design)
    # if design in special:
    #     continue
    if is_possible(design, 0, len(design), t):
        ans += 1
    # break
print('ans:', ans)