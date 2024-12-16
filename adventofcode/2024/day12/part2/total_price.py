import os
from collections import deque

ans = 0
matrix = []
grid = {}

with open(os.path.join(os.path.dirname(__file__), 'input'), encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        matrix.append(line)
        grid[(i, -1)] = "."
        for j, ch in enumerate(line):
            grid[(i, j)] = ch
        grid[(i, len(line))] = "."

row_cnt = len(matrix)
col_cnt = len(matrix[0])

for j in range(-1, col_cnt + 1):
    grid[(-1, j)] = "."
    grid[(row_cnt, j)] = "."

# print grid
# for i in range(-1, row_cnt + 1):
#     for j in range(-1, col_cnt + 1):
#         print(grid[(i, j)], end = ' ')
#     print()

def plot_neighbours(x, y):
    yield [(x, y - 1), (x - 1, y - 1), (x - 1, y)]
    yield [(x - 1, y), (x - 1, y + 1), (x, y + 1)]
    yield [(x, y + 1), (x + 1, y + 1), (x + 1, y)]
    yield [(x, y - 1), (x + 1, y - 1), (x + 1, y)]
    

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



# https://github.com/thomasjevskij/advent_of_code/blob/master/2024/aoc12/day12.py
# 计算边：
# 先把图的周围扩充一圈，用其他字符填充。
# plot_neighbours 可以生成某个点四个角，每个角周围有三个点。
# 根据这三个点的字符值跟当前点的字符值进行比较，可以确定是否为边做贡献。
# 将这三个点标号 1， 2， 3. 只有以下两种情况对边有贡献
# a) 1, 3两个点跟当前点的字符值均不同。说明这个点在这个角跟周围都不一样。是个尖尖的突出来的角。
# b) 1, 3两个点跟当前点的字符值相同，但第2个点跟当前点的字符值不同。是个凹进去的角。
def calculate_sides(region):
    side = 0
    for x, y in region:
        ch = matrix[x][y]
        for ns in plot_neighbours(x, y):
            if all(grid[(nx, ny)] != ch for nx, ny in ns[::2]) or (all(grid[(nx, ny)] == ch for nx, ny in ns[::2]) and grid[ns[1]] != ch):
                side += 1
    return side

for i, row in enumerate(matrix):
    for j, ch in enumerate(row):
        if not visited[i][j]: 
            region = search(i, j)
            area = len(region)
            sides = calculate_sides(region)
            # print(matrix[i][j], area,  sides)
            ans += area * sides
        
print('ans:', ans) # ans: 899196