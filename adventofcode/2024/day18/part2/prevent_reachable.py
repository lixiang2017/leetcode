from pathlib import Path
import os
import heapq
from collections import defaultdict

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")

corrupted = lines.split("\n")
# row_cnt = col_cnt = 7 # 71
row_cnt = col_cnt = 71
matrix = [["."] * col_cnt for _ in range(row_cnt)]


def reachable(sx, sy, ex, ey):
    # directions
    dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    # (steps, x, y)
    q = [(0, sx, sy)]
    # (x, y)
    seen = set([(0, 0)])

    while q:
        steps, x, y = heapq.heappop(q)
        if x == ex and y == ey:
            return True
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row_cnt and 0 <= ny < col_cnt and matrix[nx][ny] == "." and (nx, ny) not in seen:
                seen.add((nx, ny))
                heapq.heappush(q, (steps + 1, nx, ny))
    return False

# binary search
left, right = 0, len(corrupted) - 1
# print("corrupted ", corrupted)
while left <= right:
    mid = (left + right) // 2
    # reset matrix
    matrix = [["."] * col_cnt for _ in range(row_cnt)]
    for cor in corrupted[: mid]:
        r, c = list(map(int, cor.split(",")))
        matrix[r][c] = "#"

    if reachable(0, 0, row_cnt - 1, col_cnt - 1):
        left = mid + 1
    else:
        right = mid - 1
        ans = corrupted[mid - 1]
    
print("ans:", ans) # ans: 24,32