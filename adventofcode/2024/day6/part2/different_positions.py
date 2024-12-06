import os 
import re 

ans = 0
matrix = []
guard = "^"
x = y = 0

input_path_from_part1 = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'part1'), 'input')
with open(input_path_from_part1, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        matrix.append(list(line))
        if guard in line:
            x = len(matrix) - 1
            y = line.index(guard)

row_cnt = len(matrix)
col_cnt = len(matrix[0])
print("row_cnt ", row_cnt, "col_cnt ",  col_cnt)
gx, gy = x, y

def can_jump_out(x, y):
    # directions
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d = 0
    step = 0
    while True:
        dx, dy = dirs[d]
        while 0 <= x + dx < row_cnt and 0 <= y + dy < col_cnt and matrix[x + dx][y + dy] != "#":
            # matrix[x + dx][y + dy] = "X"
            x += dx
            y += dy
            step += 1
        if step > row_cnt * col_cnt:
            return False
        nx = x + dx
        ny = y + dy
        if not (0 <= nx < row_cnt and 0 <= ny < col_cnt):
            return True
        d += 1
        d %= 4

    return True

for i, row in enumerate(matrix):
    for j, ch in enumerate(row):
        if ch in ["#", "^"]:
            continue
        # set it to "#"
        matrix[i][j] = "#"
        if not can_jump_out(gx, gy):
            ans += 1 
            print("part ans ", ans)
        # undo
        matrix[i][j] = "."


print('ans: ', ans) # ans:  1909