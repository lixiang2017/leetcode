from pathlib import Path
import os
import heapq
from collections import defaultdict

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")

corrupted = lines.split("\n")
# row_cnt = col_cnt = 7 # 71
# first_kilobyte = 12 # 1024
row_cnt = col_cnt = 71
first_kilobyte = 1024
matrix = [["."] * col_cnt for _ in range(row_cnt)]
for cor in corrupted[: first_kilobyte]:
    r, c = list(map(int, cor.split(",")))
    matrix[r][c] = "#"

def find_min_steps(sx, sy, ex, ey):
    # directions
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    # (steps, x, y)
    q = [(0, sx, sy)]
    # (x, y)
    seen = set([(0, 0)])

    while q:
        steps, x, y = heapq.heappop(q)
        if x == ex and y == ey:
            return steps
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row_cnt and 0 <= ny < col_cnt and matrix[nx][ny] == "." and (nx, ny) not in seen:
                seen.add((nx, ny))
                # print(steps + 1, nx, ny)
                heapq.heappush(q, (steps + 1, nx, ny))

min_steps = find_min_steps(0, 0, row_cnt - 1, col_cnt - 1)
print("ans:", min_steps) # ans: 302