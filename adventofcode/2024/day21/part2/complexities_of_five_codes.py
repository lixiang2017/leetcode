'''
https://www.reddit.com/r/adventofcode/comments/1hj2odw/2024_day_21_solutions/?sort=confidence
fragger
[Language: Python] 900/638
Wow I really enjoyed this problem, what a rush getting everything to work for part 2 after my brain stopped melting. Woohoo, first sub 1k on part 1 and/or part 2 this year. Maybe I'll make a leaderboard spot yet. :)

I started out part 1 just trying to get output like the examples for debugging since I figured I'd need it, that definitely didn't scale for part 2 and was already very slow for part 1. While rewriting my function to just return the length of the shortest sequence it could generate and also do that for n depth, it finally clicked in my head that every sub sequence press needing to end in an 'A' means that the location of each robot does not need to be tracked after it finishes its sub sequence and thus the problem breaks down neatly recursively.

https://github.com/Fragger/advent-of-code/blob/master/2024/solution/21.py (59 lines)
'''
import os
from functools import cache
from itertools import permutations

with open(os.path.join(os.path.dirname(__file__), 'input'), encoding="utf-8") as f:
    codes = f.read().splitlines()

numkeypad = ['789',
             '456',
             '123',
             ' 0A']
numkeypad = {key: (x, y) for y, line in enumerate(numkeypad) for x, key in enumerate(line) if key != ' '}

dirkeypad = [' ^A',
             '<v>']
dirkeypad = {key: (x, y) for y, line in enumerate(dirkeypad) for x, key in enumerate(line) if key != ' '}

dirs = {'^': (0, -1), '>': (1, 0), 'v': (0, 1), '<': (-1, 0)}

@cache
def get_presses(sequence, depth=2, dirkey=False, cur=None):
    keypad = dirkeypad if dirkey else numkeypad
    if not sequence:
        return 0
    if not cur:
        cur = keypad['A']

    cx, cy = cur
    px, py = keypad[sequence[0]]
    dx, dy = px-cx, py-cy

    buttons = '>'*dx + '<'*-dx + 'v'*dy + '^'*-dy

    if depth:
        perm_lens = []
        for perm in set(permutations(buttons)):
            cx, cy = cur
            for button in perm:
                dx, dy = dirs[button]
                cx += dx
                cy += dy
                if (cx, cy) not in keypad.values():
                    break
            else:
                perm_lens.append(get_presses(perm+('A',), depth-1, True))
        min_len = min(perm_lens)
    else:
        min_len = len(buttons)+1
    return min_len+get_presses(sequence[1:], depth, dirkey, (px, py))

p1 = 0
p2 = 0
for code in codes:
    codenum = int(code[:-1])
    p1 += codenum*get_presses(code)
    p2 += codenum*get_presses(code, 25)

print(p1)
print(p2)