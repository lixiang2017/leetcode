from pathlib import Path
import os
import heapq
from collections import defaultdict, deque
from itertools import pairwise
from functools import cache

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")

codes = lines.split("\n")

# The numeric keypad
numeric = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]
numeric = tuple(tuple(t) for t in numeric)
# The directional keypad
directional = [["#", "^", "A"], ["<", "v", ">"]]
directional = tuple(tuple(t) for t in directional)

@cache
def find_path(keypad, start, end):
    row_cnt, col_cnt = len(keypad), len(keypad[0])
    sx = sy = ex = ey = 0
    for i, row in enumerate(keypad):
        for j, ch in enumerate(row):
            if ch == start:
                sx, sy = i, j
            if ch == end:
                ex, ey = i, j
    
    directions = [(-1, 0, "^"), (0, 1, ">"),  (1, 0, "v"),  (0, -1, "<")]
    q = deque([(sx, sy, "")])
    seen = {(sx, sy)}
    while q:
        x, y, path = q.popleft()
        if x == ex and y == ey:
            return path
        for dx, dy, ch in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row_cnt and 0 <= ny < col_cnt and keypad[nx][ny] != "#" and (nx, ny) not in seen:
                q.append((nx, ny, path + ch))
 
@cache
def find_all_paths(keypad, start, end, max_len):
    row_cnt, col_cnt = len(keypad), len(keypad[0])
    sx = sy = ex = ey = 0
    for i, row in enumerate(keypad):
        for j, ch in enumerate(row):
            if ch == start:
                sx, sy = i, j
            if ch == end:
                ex, ey = i, j
    
    directions = [(-1, 0, "^"), (0, 1, ">"),  (1, 0, "v"),  (0, -1, "<")]
    q = deque([(sx, sy, "", ((sx, sy), ) )])
    paths = []
    while q:
        x, y, path, seen_path = q.popleft()
        if x == ex and y == ey:
            paths.append(path)
            continue
        if len(seen_path) > max_len or len(path) > max_len:
            continue
        for dx, dy, ch in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row_cnt and 0 <= ny < col_cnt and keypad[nx][ny] != "#" and (nx, ny) not in seen_path:
                q.append((nx, ny, path + ch, seen_path + ((nx, ny),) ))
    return paths

@cache
def directional_to_numeric(code):
    decoded = ['']
    for a, b in pairwise("A" + code):
        paths = find_all_paths(numeric, a, b, 6)
        decoded = [d + path + "A" for d in decoded for path in paths]
    
    min_len = min(len(d) for d in decoded)
    decoded = tuple(d for d in decoded if min_len == len(d))
    return decoded

@cache
def directional_to_directional(code_list):
    all_decoded = set()
    for _code in code_list:
        decoded = ['']
        for a, b in pairwise("A" + _code):
            path = find_path(directional, a, b)
            paths = find_all_paths(directional, a, b, len(path))
            decoded = set([d + path + "A" for d in decoded for path in paths])
        
        all_decoded.update(decoded)
    
    min_len = min(len(d) for d in all_decoded)
    all_decoded = tuple(d for d in all_decoded if min_len == len(d))
    return all_decoded


def simulate(code):
    decoded = directional_to_numeric(code)
    for _ in range(2):
        decoded = directional_to_directional(decoded)
    return min(len(d) for d in decoded)

def numeric_part(code):
    return int(code[: -1])

for code in codes:
    s = simulate(code)
    n = numeric_part(code)
    print(code, s, n)
    ans += s * n
    
print("ans: ", ans) # ans:  164960