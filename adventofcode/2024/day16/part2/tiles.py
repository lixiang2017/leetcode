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
lowest_score = 0

while q:
    score, x, y, d = heapq.heappop(q)
    # print(score, x, y, d)
    seen.add((x, y, d))
    if x == ex and y == ey:
        lowest_score = score
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


print("lowest_score ", lowest_score)

# warning! should reset initial direction!
print("current d", d)
d = 0
# (score, x, y, d, path)
q = [(0, sx, sy, d, [(sx, sy)])]
# (x, y, d)
seen = set()
best_paths = set()

while q:
    score, x, y, d, path = heapq.heappop(q)
    # print(score, x, y, d)
    seen.add((x, y, d))
    if x == ex and y == ey and score == lowest_score:
        best_paths.add(tuple(path))
        print(len(path))
        continue
    # move
    dx, dy = dirs[d]
    nx, ny = x + dx, y + dy
    if 0 < nx < row_cnt - 1 and 0 < ny < col_cnt - 1 and matrix[nx][ny] in [".", "E"] and (nx, ny, d) not in seen and score + 1 <= lowest_score:
        heapq.heappush(q, (score + 1, nx, ny, d, path + [(nx, ny)]))
    # turn left
    if (x, y, (d + 1) % 4) not in seen and score + 1000 <= lowest_score:
        heapq.heappush(q, (score + 1000, x, y, (d + 1) % 4, path))
    # turn right
    if (x, y, (d - 1) % 4) not in seen and score + 1000 <= lowest_score:
        heapq.heappush(q, (score + 1000, x, y, (d - 1) % 4, path))


print("count best_path: ", len(best_paths))


best_spot = [[False] * col_cnt for _ in range(row_cnt)]
for path in best_paths:
    for x, y in path:
        best_spot[x][y] = True

# print best_spot
# for row in best_spot:
#     print("".join("O" if r else "." for r in row))

ans = sum(sum(row) for row in best_spot)
print("ans: ", ans) # ans:  593
