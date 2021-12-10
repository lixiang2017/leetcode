





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

    for i in range(m):
        for j in range(n):
            is_low = True
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] <= grid[i][j]:
                    is_low = False
                    break
            if is_low:
                # print(grid[i][j])
                risk += grid[i][j] + 1

    print('risk: ', risk)
    return risk 


r1 = get_risk_level('input1')
r = get_risk_level('input')


'''
risk:  15
risk:  491
'''

