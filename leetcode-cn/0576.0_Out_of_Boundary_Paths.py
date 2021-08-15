'''
73 / 94 个通过测试用例
状态：超出时间限制
提交时间：几秒前
最后执行的输入：
7
6
13
0
2
'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        q = deque([(startRow, startColumn, maxMove)])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def inArea(i, j):
            return 0 <= i < m and 0 <= j < n

        while q:
            r, c, move = q.popleft()
            if move > 0:
                for deltar, deltac in dirs:
                    nr, nc = r + deltar, c + deltac
                    if inArea(nr, nc):
                        q.append((nr, nc, move - 1))
                    else:
                        ans += 1

        return ans % MOD



'''
DFS

执行用时：96 ms, 在所有 Python3 提交中击败了89.62% 的用户
内存消耗：21 MB, 在所有 Python3 提交中击败了19.38% 的用户
'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        q = deque([(startRow, startColumn, maxMove)])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def inArea(i, j):
            return 0 <= i < m and 0 <= j < n

        @cache
        def dfs(i, j, move):
            if 0 > move:
                return 0
            if not inArea(i, j):
                return 1
            ans = 0
            for deltar, deltac in dirs:
                ni, nj = i + deltar, j + deltac
                ans += dfs(ni, nj, move - 1)
            return ans

        return dfs(startRow, startColumn, maxMove) % MOD
