from pathlib import Path
import os
import heapq

ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")


matrix = lines.split("\n")

print("matrix ", matrix)

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

# directions
dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
# initial d
d = 0

print(sx, sy, ex, ey)

# (score, x, y, d)
q = [(0, sx, sy, d)]
# (x, y, d)
seen = set()

while q:
    score, x, y, d = heapq.heappop(q)
    # print(score, x, y, d)
    seen.add((x, y, d))
    if x == ex and y == ey:
        print("ans = score ", ans, score)
        ans = score
        break
    # move
    dx, dy = dirs[d]
    nx, ny = x + dx, y + dy
    if 0 < nx < row_cnt - 1 and 0 < ny < col_cnt - 1 and matrix[nx][ny] in [".", "E"] and (nx, ny, d) not in seen:
        heapq.heappush(q, (score + 1, nx, ny, d))
    # turn left
    if (x, y, (d + 1) % 4) not in seen:
        heapq.heappush(q, (score + 1000, x, y, (d + 1) % 4))
    # turn right
    if (x, y, (d - 1) % 4) not in seen:
        heapq.heappush(q, (score + 1000, x, y, (d - 1) % 4))

print("ans: ", ans) # ans:  143564
