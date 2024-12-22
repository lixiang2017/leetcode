# https://github.com/matheusstutzel/adventOfCode/blob/main/2024/20/p2.py

from pathlib import Path
import os
import heapq
from collections import defaultdict

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")


matrix = lines.split("\n")
matrix = [list(row) for row in matrix]
# print("matrix ", matrix)
row_cnt = len(matrix)
col_cnt = len(matrix[0])


# start, end
sx = sy = ex = ey = 0
for i, row in enumerate(matrix):
    for j, ch in enumerate(row):
        if ch == 'S':
            sx, sy = i, j
        if ch == 'E':
            ex, ey = i, j
print(sx, sy, ex, ey)

def fewest_picoseconds(sx, sy, ex, ey):
    # directions
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    # (picoseconds, x, y)
    q = [(0, sx, sy)]
    # (x, y)
    seen = set()
    # distance
    dist = {}

    while q:
        picoseconds, x, y = heapq.heappop(q)
        seen.add((x, y))
        dist[(x, y)] = picoseconds
        if x == ex and y == ey:
            return picoseconds, dist
        # move
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 < nx < row_cnt - 1 and 0 < ny < col_cnt - 1 and matrix[nx][ny] in [".", "E"] and (nx, ny) not in seen:
                heapq.heappush(q, (picoseconds + 1, nx, ny))
                break


fewest, dist = fewest_picoseconds(sx, sy, ex, ey)
print("fewest_picoseconds ", fewest)

def manhattan(v1, v2):
    return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])

for v1, d1 in dist.items():
    for v2, d2 in dist.items():
        m = manhattan(v1, v2)
        if m <= 20 and d1 - d2 - m >= 100:
            ans += 1
print("ans: ", ans) # ans:  1010263
