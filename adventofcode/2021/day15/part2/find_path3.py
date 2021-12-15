
from collections import deque 
from heapq import heappop, heappush
import math

def lowerest_total_risk(file_name):
    grid = []

    with open(file_name) as f:
        for line in f:
            line = line.strip()
            grid.append(list(map(int, list(line))))
    
    m, n = len(grid), len(grid[0])
    
    # large grid
    lgrid = [[0] * (n * 5) for _ in range(m * 5)]
    dp = [[math.inf] * (n * 5) for _ in range(m * 5)]

    for i in range(m * 5):
        for j in range(n * 5):
            # fold, remainder
            fi, ri= divmod(i, m)
            fj, rj = divmod(j, n)
            lgrid[i][j] = (grid[ri][rj] - 1 + fi + fj) % 9 + 1 

    q = deque([(0, 0, lgrid[0][0])])
    dp[0][0] = 0
    while q:
        cost, i, j = q.popleft()
        print(cost, i, j)
        if i == m * 5 - 1 and j == n * 5 - 1:
            print(dp[i][j])     
            break   
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < m * 5 and 0 <= nj < n * 5:
                if cost + lgrid[ni][nj] < dp[ni][nj]:
                    dp[ni][nj] = cost + lgrid[ni][nj]
                    q.append((dp[ni][nj], ni, nj))

    print('lowerest_total_risk: ', dp[-1][-1])
    return dp[-1][-1]

l1 = lowerest_total_risk('input1')
l = lowerest_total_risk('input')

'''
还是需要用优先队列。不用优先队列，只是用BFS，跑半天也跑不出来。
'''

