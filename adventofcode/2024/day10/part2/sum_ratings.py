import os

ans = 0
matrix = []
# 0 position list
zero = []

with open(os.path.join(os.path.dirname(__file__), 'input'), encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        matrix.append(line)
        for j, ch in enumerate(line):
            if "0" == ch:
                zero.append([i, j])

row_cnt = len(matrix)
col_cnt = len(matrix[0])

def rating(zx, zy):
    # set of distinct hiking trails
    trails = set()
    
    def search(current, x, y, path):
        if current == 9:
            trails.add(tuple(path))
            return
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row_cnt and 0 <= ny < col_cnt and matrix[nx][ny] != "." and int(matrix[nx][ny]) == current + 1:
                search(current + 1, nx, ny, path + [(nx, ny)])
    
    search(0, zx, zy, [(zx, zy)])
    return len(trails)
    
for zx, zy in zero:
    ans += rating(zx, zy)

print('ans:', ans) # ans: 1034