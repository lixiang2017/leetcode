import os
from collections import deque

ans = 0
matrix = []

with open(os.path.join(os.path.dirname(__file__), 'input'), encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        matrix.append(line)

row_cnt = len(matrix)
col_cnt = len(matrix[0])

visited = [[False] * col_cnt for _ in range(row_cnt)]

def search(i, j):
    plant = matrix[i][j]
    seen = {(i, j)}
    q = deque([(i, j)])
    while q:
        i, j = q.popleft()
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < row_cnt and 0 <= nj < col_cnt and not visited[ni][nj] and (ni, nj) not in seen and matrix[ni][nj] == plant:
                seen.add((ni, nj))
                visited[ni][nj] = True
                q.append((ni, nj))
    return seen

def calculate_perimeter(region):
    p = 0
    current_seen = set()
    for i, j in region:
        touching_cnt = 0
        for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= ni < row_cnt and 0 <= nj < col_cnt and (ni, nj) in region and (ni, nj) not in current_seen:
                touching_cnt += 1
        p += 4 - touching_cnt * 2
        current_seen.add((i, j))
    return p

for i, row in enumerate(matrix):
    for j, ch in enumerate(row):
        if not visited[i][j]:
            region = search(i, j)
            area = len(region)
            perimeter = calculate_perimeter(region)
            print(ch, area, perimeter)
            ans += area * perimeter
        
print('ans:', ans) # ans: 1485656