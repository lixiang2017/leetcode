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

    while q:
        picoseconds, x, y = heapq.heappop(q)
        seen.add((x, y))
        if x == ex and y == ey:
            return picoseconds
        # move
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 < nx < row_cnt - 1 and 0 < ny < col_cnt - 1 and matrix[nx][ny] in [".", "E"] and (nx, ny) not in seen:
                heapq.heappush(q, (picoseconds + 1, nx, ny))

fewest = fewest_picoseconds(sx, sy, ex, ey)
print("fewest_picoseconds ", fewest)


def cheats0():
    # wrong, don't need to consider neighbours
    picos = defaultdict(int)
    for i in range(1, row_cnt - 2):
        for j in range(1, col_cnt - 2):
            # row
            if "#" in [matrix[i][j], matrix[i][j + 1]]:
                ch1, ch2 = matrix[i][j], matrix[i][j + 1]
                if matrix[i][j] == "#":
                    matrix[i][j] = "."
                if matrix[i][j + 1] == "#":
                    matrix[i][j + 1] = "."
                pico = fewest_picoseconds(sx, sy, ex, ey)
                matrix[i][j], matrix[i][j + 1] = ch1, ch2
                picos[pico] += 1
            # col
            if "#" in [matrix[i][j], matrix[i + 1][j]]:
                ch1, ch2 = matrix[i][j], matrix[i + 1][j]
                if matrix[i][j] == "#":
                    matrix[i][j] = "."
                if matrix[i + 1][j] == "#":
                    matrix[i + 1][j] = "."
                pico = fewest_picoseconds(sx, sy, ex, ey)
                matrix[i][j], matrix[i + 1][j] = ch1, ch2
                picos[pico] += 1
    return picos

def cheats():
    # right
    picos = defaultdict(int)
    for i in range(row_cnt - 1):
        for j in range(col_cnt - 1):
            if "#"  == matrix[i][j]:
                ch1 = matrix[i][j]
                matrix[i][j] = "."
                pico = fewest_picoseconds(sx, sy, ex, ey)
                matrix[i][j] = ch1
                picos[pico] += 1
    return picos


picos = cheats()
for p, cnt in sorted(picos.items(), key=lambda pair: -pair[0]):
    print(f"There are {cnt} cheats that save {fewest - p} picoseconds.")
    if fewest - p >= 100:
        ans += cnt

print("ans: ", ans) # ans:  1411
