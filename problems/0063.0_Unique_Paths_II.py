'''
DP
T: O(MN)
S: O(MN)

Runtime: 36 ms, faster than 95.05% of Python3 online submissions for Unique Paths II.
Memory Usage: 14.4 MB, less than 33.48% of Python3 online submissions for Unique Paths II.
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        m, n = len(g), len(g[0])
        path = [[0] * n for _ in range(m)]
        path[0][0] = 1 if g[0][0] != 1 else 0
        for i in range(m):
            for j in range(n):
                if g[i][j] == 1:
                    continue
                for x, y in [(i - 1, j), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n:
                        # print(i, j, x, y)
                        path[i][j] += path[x][y]
        
        return path[-1][-1]

'''
[[0,0,0],[0,1,0],[0,0,0]]
[[0,1],[0,0]]
[[0,0],[0,1]]
[[0,0]]
'''

'''
Input
[[1]]
Output
1
Expected
0
'''


'''
DP
T: O(MN)
S: O(MN)

Runtime: 48 ms, faster than 32.75% of Python3 online submissions for Unique Paths II.
Memory Usage: 14.1 MB, less than 95.66% of Python3 online submissions for Unique Paths II.
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        m, n = len(g), len(g[0])
        path = [[0] * (n + 1) for _ in range(m + 1)]
        path[1][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for x, y in [[i - 1, j], [i, j - 1]]:
                    # origin x, y in grid
                    ox, oy = x - 1, y - 1
                    if 0 <= ox < m and 0 <= oy < n and g[ox][oy] == 0:
                        path[i][j] += path[x][y]

        return [path[-1][-1], 0][g[-1][-1] == 1] 
        

'''
DP
T: O(MN)
S: O(MN)

Runtime: 56 ms, faster than 53.18% of Python3 online submissions for Unique Paths II.
Memory Usage: 13.9 MB, less than 74.88% of Python3 online submissions for Unique Paths II.
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0]) if obstacleGrid else 0 
        if 0 == m or 0 == n or 1 == obstacleGrid[0][0] or 1 == obstacleGrid[-1][-1]:
            return 0
        path = [[0] * (n + 1) for _ in range(m + 1)]
        path[0][1] = 1
        for i in range(m):
            for j in range(n):
                if 1 == obstacleGrid[i][j]:
                    continue
                path[i + 1][j + 1] = path[i + 1][j] + path[i][j + 1]
        
        return path[m][n]
        

'''
DP
T: O(MN)
S: O(1)

Runtime: 103 ms, faster than 5.10% of Python3 online submissions for Unique Paths II.
Memory Usage: 13.9 MB, less than 96.86% of Python3 online submissions for Unique Paths II.
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        g = obstacleGrid
        m, n = len(g), len(g[0]) if g else 0 
        # no paths to the destination
        if 0 == m or 0 == n or 1 == g[0][0] or 1 == g[-1][-1]:
            return 0
        # number of ways of reaching the starting cell = 1.
        g[0][0] = 1
        # filling the values for the first column
        for i in range(1, m):
            g[i][0] = int(g[i][0] == 0 and g[i - 1][0] == 1)
        # filling the values for the first row
        for j in range(1, n):
            g[0][j] = int(g[0][j] == 0 and g[0][j - 1] == 1)
        # starting from cell(1, 1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. from above and left
        for i in range(1, m):
            for j in range(1, n):
                if 0 == g[i][j]:
                    g[i][j] = g[i - 1][j] + g[i][j - 1]
                else:
                    g[i][j] = 0
        
        return g[-1][-1]
        
