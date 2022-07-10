'''
DFS + memoization

执行用时：524 ms, 在所有 Python3 提交中击败了43.14% 的用户
内存消耗：70.5 MB, 在所有 Python3 提交中击败了6.37% 的用户
通过测试用例：59 / 59
'''
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @cache
        def dfs(r1, c1, r2, c2):
            if not (0 <= min(r1, c1, r2, c2) < n and 0 <= max(r1, c1, r2, c2) < n):
                return float('-inf')
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if r1 == c1 == n - 1:
                return grid[-1][-1]
            total = 0
            if r1 == r2:  # must have c1 == c2
                total += grid[r1][c1]
            else:
                total += grid[r1][c1] + grid[r2][c2]
            p1 = dfs(r1 + 1, c1, r2 + 1, c2)
            p2 = dfs(r1 + 1, c1, r2, c2 + 1)
            p3 = dfs(r1, c1 + 1, r2 + 1, c2)
            p4 = dfs(r1, c1 + 1, r2, c2 + 1)
            total += max(p1, p2, p3, p4)
            return total 

        return max(0, dfs(0, 0, 0, 0))

