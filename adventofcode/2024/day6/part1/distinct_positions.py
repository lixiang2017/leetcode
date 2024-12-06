import os 
import re 

ans = 0
matrix = []
guard = "^"
x = y = 0

with open(os.path.join(os.path.dirname(__file__), 'input'), encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        matrix.append(list(line))
        if guard in line:
            x = len(matrix) - 1
            y = line.index(guard)

row_cnt = len(matrix)
col_cnt = len(matrix[0])

def predict(x, y):
    # directions
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    d = 0
    while True:
        dx, dy = dirs[d]
        while 0 <= x + dx < row_cnt and 0 <= y + dy < col_cnt and matrix[x + dx][y + dy] != "#":
            matrix[x + dx][y + dy] = "X"
            x += dx
            y += dy
        nx = x + dx
        ny = y + dy
        if not (0 <= nx < row_cnt and 0 <= ny < col_cnt):
            return
        d += 1
        d %= 4

predict(x, y)
ans = sum(ch == "X" or ch == "^" for i, row in enumerate(matrix) for j, ch in enumerate(row))
print('ans: ', ans) # ans:  5162