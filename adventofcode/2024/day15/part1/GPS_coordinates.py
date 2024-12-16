from pathlib import Path
import os
import re


ans = 0
file_path = os.path.join(os.path.dirname(__file__), 'input')
lines = Path(file_path).read_text(encoding="utf-8")
groups = re.split("\n\n", lines)

print(len(groups))
warehouse, movements = groups

matrix = warehouse.split("\n")

print("matrix ", matrix)

row_cnt = len(matrix)
col_cnt = len(matrix[0])

# robot
x = 0
y = 0
grid = []
for i, row in enumerate(matrix):
    grid.append(list(row))
    if "@" in row:
        x = i
        y = row.index("@")

def move(m):
    # original x, y
    global x
    global y
    ox, oy = x, y
    d = 0
    found = has_O = False
    match m:
        case "<":
            while y - d > 0 and grid[x][y - d] != "#":
                if grid[x][y - d] == "O":
                    has_O = True
                if grid[x][y - d] == ".":
                    found = True
                    break
                d += 1
            if found:
                if has_O:
                    grid[x][y - d] = "O"
                y -= 1
                grid[x][y] = "@"
                grid[ox][oy] = '.'
        case ">":
            while y + d < col_cnt and grid[x][y + d] != "#":
                if grid[x][y + d] == "O":
                    has_O = True
                if grid[x][y + d] == ".":
                    found = True
                    break
                d += 1
            if found:
                if has_O:
                    grid[x][y + d] = "O"
                y += 1
                grid[x][y] = "@"
                grid[ox][oy] = '.'
        case "^":
            while x - d > 0 and grid[x - d][y] != "#":
                if grid[x - d][y] == "O":
                    has_O = True
                if grid[x - d][y] == ".":
                    found = True
                    break
                d += 1
            if found:
                if has_O:
                    grid[x - d][y] = "O"
                x -= 1
                grid[x][y] = "@"
                grid[ox][oy] = '.'
        case "v":
            while x + d < row_cnt and grid[x + d][y] != "#":
                if grid[x + d][y] == "O":
                    has_O = True
                if grid[x + d][y] == ".":
                    found = True
                    break
                d += 1
            if found:
                if has_O:
                    grid[x + d][y] = "O"
                x += 1
                grid[x][y] = "@"
                grid[ox][oy] = '.'

print("start ", x, y)

for row in movements:
    for m in row:
        # print(m)
        move(m)


for i in range(1, row_cnt):
    for j in range(col_cnt):
        if grid[i][j] == "O":
            ans += 100 * i + j

print('ans:', ans) # ans: 1497888