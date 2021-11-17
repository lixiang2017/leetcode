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
        


