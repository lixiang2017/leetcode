import os 
from collections import defaultdict

ans = 0
matrix = []
# ch -> position list
positions = defaultdict(list)

with open(os.path.join(os.path.dirname(__file__), 'input'), encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        matrix.append(line)
        for j, ch in enumerate(line):
            if "." != ch and "#" != ch:
                positions[ch].append([i, j])

row_cnt = len(matrix)
col_cnt = len(matrix[0])

contain = [[False] * col_cnt for _ in range(row_cnt)]

for ch, position_list in positions.items():
    total = len(position_list)
    if total > 1:
        for i in range(total - 1):
            for j in range(i + 1, total):
                x1, y1 = position_list[i]
                x2, y2 = position_list[j]
                contain[x1][y1] = True
                contain[x2][y2] = True
                
                dx, dy = x2 - x1, y2 - y1
                nx1, ny1 = x1 - dx, y1 - dy
                while 0 <= nx1 < row_cnt and 0 <= ny1 < col_cnt:
                    contain[nx1][ny1] = True
                    nx1 -= dx
                    ny1 -= dy

                nx2, ny2 = x2 + dx, y2 + dy
                while 0 <= nx2 < row_cnt and 0 <= ny2 < col_cnt:
                    contain[nx2][ny2] = True
                    nx2 += dx
                    ny2 += dy

ans = sum(sum(row) for row in contain)
print('ans: ', ans) # ans:  955