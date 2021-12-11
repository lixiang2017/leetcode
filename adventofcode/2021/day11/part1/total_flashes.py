
from collections import deque

def get_total(file_name, round):
    total = 0

    grid = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            grid.append(list(map(int, list(line))))

    m, n = len(grid), len(grid[0])
    for _ in range(round):
        flashed = set()
        q = deque()
        for i in range(m):
            for j in range(n):
                grid[i][j] += 1
                if grid[i][j] == 10:
                    flashed.add((i, j))
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    grid[ni][nj] += 1
                    if grid[ni][nj] == 10:
                        flashed.add((ni, nj))
                        q.append((ni, nj))                        

        # set to 0 after flash
        for i, j in flashed:
            grid[i][j] = 0

        total += len(flashed)
        flashed.clear()

    print('total: ', total)
    return total



c1 = get_total('input1', 10)
c2 = get_total('input1', 100)
c = get_total('input', 100)

'''
total:  204
total:  1656
total:  1725
'''

