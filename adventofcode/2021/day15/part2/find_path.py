


def lowerest_total_risk(file_name):
    grid = []

    with open(file_name) as f:
        for line in f:
            line = line.strip()
            grid.append(list(map(int, list(line))))
    
    m, n = len(grid), len(grid[0])
    
    # large grid
    lgrid = [[0] * n * 5 for _ in range(m * 5)]
    dp = [[0] * n * 5 for _ in range(m * 5)]

    for i in range(m * 5):
        for j in range(n * 5):
            # fold, remainder
            fi, ri= divmod(i, m)
            fj, rj = divmod(j, n)
            x = (grid[ri][rj] + fi + fj)
            if x > 9:
                lgrid[i][j] = x - 9
            else:
                lgrid[i][j] = x

    lgrid[0][0] = 0
    for i in range(m * 5):
        for j in range(n * 5):
            if i == 0:
                if j > 0:
                    dp[i][j] = dp[i][j - 1] + lgrid[i][j]
            else:
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + lgrid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + lgrid[i][j]

    print('lowerest: ', dp[-1][-1])
    return dp[-1][-1] 

l1 = lowerest_total_risk('input1')
l = lowerest_total_risk('input')

'''
# wrong!!! 4 directions!
lowerest:  315
lowerest:  2973
'''

