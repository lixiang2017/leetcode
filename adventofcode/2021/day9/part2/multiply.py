


import heapq


def get_risk_level(file_name):
    # print('================')
    risk = 0
    m = n = 0
    grid = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            n = len(line)
            grid.append(line)
    m = len(grid)
    grid = [list(map(int, list(row))) for row in grid]

    # low points
    low = []
    for i in range(m):
        for j in range(n):
            is_low = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] <= grid[i][j]:
                    is_low = False
                    break
            if is_low:
                low.append([i, j])

    seen = set()
    def get_basin_size(i, j):
        s = 1 
        nonlocal seen
        seen.add((i, j))
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen and grid[ni][nj] != 9:
                ns = get_basin_size(ni, nj)
                s += ns
        
        return s     

    # basin size list
    bs = []
    for i, j in low:
        s = get_basin_size(i, j)
        heapq.heappush(bs, -s)

    multi = 1
    for _ in range(3):
        s = - heapq.heappop(bs)
        print('s: ', s)
        multi *= s 
    print('multi: ', multi)
    return multi 


r1 = get_risk_level('input1')
r = get_risk_level('input')


'''
s:  14
s:  9
s:  9
multi:  1134
s:  112
s:  99
s:  97
multi:  1075536
'''



