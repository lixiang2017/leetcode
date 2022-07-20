'''
simulation

执行用时：52 ms, 在所有 Python3 提交中击败了71.62% 的用户
内存消耗：15.3 MB, 在所有 Python3 提交中击败了46.72% 的用户
通过测试用例：107 / 107
'''
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0]) if grid else 0
        k %= m * n
        ans = [[0] * n for _ in range(m)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                idx = i * n + j
                ni, nj = divmod((idx + k) % (m * n), n)
                ans[ni][nj] = x 
        return ans 

