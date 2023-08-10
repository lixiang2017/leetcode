'''
时间 656 ms 击败 25.16%
内存 17.6 MB 击败 99.35%
'''
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        matrix = grid
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(matrix[i - 1][: j] + matrix[i - 1][j + 1:])
        return min(matrix[-1])


'''
时间 80ms
击败 74.84%使用 Python3 的用户
内存 18.95mb
击败 38.06%使用 Python3 的用户
'''
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        for i in range(1, n):
            last_row = [(x, j) for j, x in enumerate(grid[i - 1])]
            top2 = nsmallest(2, last_row)
            for j in range(n):
                if j == top2[0][1]:
                    grid[i][j] += top2[1][0]
                else:
                    grid[i][j] += top2[0][0]
        return min(grid[-1])

