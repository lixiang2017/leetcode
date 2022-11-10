'''
执行用时：4896 ms, 在所有 Python3 提交中击败了17.14% 的用户
内存消耗：33.2 MB, 在所有 Python3 提交中击败了31.43% 的用户
通过测试用例：56 / 56
'''
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for x, y in mines:
            grid[x][y] = 0
        up, down, left, right = deepcopy(grid), deepcopy(grid), deepcopy(grid), deepcopy(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if i > 0:
                        up[i][j] = up[i - 1][j] + 1
                    if j > 0:
                        left[i][j] = left[i][j - 1] + 1
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if grid[i][j] == 1:
                    if i < n - 1:
                        down[i][j] = down[i + 1][j] + 1
                    if j < n - 1:
                        right[i][j] = right[i][j + 1] + 1
        ans = 0
        for i in range(n):
            for j in range(n):
                order = min(up[i][j], down[i][j], left[i][j], right[i][j])
                ans = max(ans, order)
        return ans 
        