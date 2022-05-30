'''
DP, T: O(MN), S: O(1)

执行用时：68 ms, 在所有 Python3 提交中击败了9.73% 的用户
内存消耗：16.3 MB, 在所有 Python3 提交中击败了82.22% 的用户
通过测试用例：61 / 61
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = grid
        m, n = len(g), len(g[0]) if g else 0
        if 0 == m or 0 == n:
            return 0
        # first row
        for j in range(1, n):
            g[0][j] += g[0][j - 1]
        # first column
        for i in range(1, m):
            g[i][0] += g[i - 1][0]
        for i in range(1, m):
            for j in range(1, n):
                g[i][j] += min(g[i - 1][j], g[i][j - 1])
        return g[-1][-1]


'''
DFS + cache

执行用时：60 ms, 在所有 Python3 提交中击败了20.71% 的用户
内存消耗：20.6 MB, 在所有 Python3 提交中击败了5.07% 的用户
通过测试用例：61 / 61
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = grid
        m, n = len(g), len(g[0]) if g else 0

        @cache
        def path_sum(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if i == 0 and j == 0:
                return g[0][0]
            if i == 0:
                return g[0][j] + path_sum(0, j - 1)
            if j == 0:
                return g[i][0] + path_sum(i - 1, 0)
            return g[i][j] + min(path_sum(i - 1, j), path_sum(i, j - 1))
        
        return path_sum(m - 1, n - 1)


'''
DFS + lru_cache

执行用时：776 ms, 在所有 Python3 提交中击败了6.38% 的用户
内存消耗：16 MB, 在所有 Python3 提交中击败了90.30% 的用户
通过测试用例：61 / 61
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = grid
        m, n = len(g), len(g[0]) if g else 0

        @lru_cache
        def path_sum(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if i == 0 and j == 0:
                return g[0][0]
            if i == 0:
                return g[0][j] + path_sum(0, j - 1)
            if j == 0:
                return g[i][0] + path_sum(i - 1, 0)
            return g[i][j] + min(path_sum(i - 1, j), path_sum(i, j - 1))
        
        return path_sum(m - 1, n - 1)



'''
DFS + memoization

执行用时：60 ms, 在所有 Python3 提交中击败了20.61% 的用户
内存消耗：17.1 MB, 在所有 Python3 提交中击败了5.07% 的用户
通过测试用例：61 / 61
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = grid
        m, n = len(g), len(g[0]) if g else 0
        s = [[-1] * n for _ in range(m)]

        def path_sum(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if s[i][j] != -1:
                return s[i][j]
            if i == 0 and j == 0:
                s[i][j] = g[0][0]
            elif i == 0:
                s[i][j] = g[0][j] + path_sum(0, j - 1)
            elif j == 0:
                s[i][j] = g[i][0] + path_sum(i - 1, 0)
            else:
                s[i][j] = g[i][j] + min(path_sum(i - 1, j), path_sum(i, j - 1))
            return s[i][j]
        
        return path_sum(m - 1, n - 1)


