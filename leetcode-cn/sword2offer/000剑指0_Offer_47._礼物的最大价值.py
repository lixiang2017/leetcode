'''
DP
T: O(MN)
S: O(1)

执行用时：56 ms, 在所有 Python3 提交中击败了30.10% 的用户
内存消耗：17 MB, 在所有 Python3 提交中击败了29.45% 的用户
通过测试用例：61 / 61
'''
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += max(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
