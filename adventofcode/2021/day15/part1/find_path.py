


def lowerest_total_risk(file_name):
    grid = []

    with open(file_name) as f:
        for line in f:
            line = line.strip()
            grid.append(list(map(int, list(line))))
    grid[0][0] = 0
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0:
                if j > 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
            else:
                if j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    print('lowerest: ', dp[-1][-1])
    return dp[-1][-1] 

l1 = lowerest_total_risk('input1')
l = lowerest_total_risk('input')
