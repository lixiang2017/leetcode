'''
T: O(2 * N * N)
S: O(2 * N)

执行用时：52 ms, 在所有 Python3 提交中击败了11.57% 的用户
内存消耗：15 MB, 在所有 Python3 提交中击败了72.68% 的用户
通过测试用例：133 / 133
'''
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        south, west = [0] * n, [0] * n
        for i in range(n):
            for j in range(n):
                south[j] = max(south[j], grid[i][j])
                west[i] = max(west[i], grid[i][j])
        inc = 0
        for i in range(n):
            for j in range(n):
                inc += min(south[j], west[i]) - grid[i][j]
        return inc 
