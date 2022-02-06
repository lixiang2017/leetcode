'''
BFS

执行用时：1564 ms, 在所有 Python3 提交中击败了12.38% 的用户
内存消耗：132.2 MB, 在所有 Python3 提交中击败了5.45% 的用户
通过测试用例：51 / 51
'''
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = deque()
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    q.append((i, j, grid[i][j], set([i * n + j, ])))

        while q:
            i, j, amount, seen = q.popleft()
            ans = max(ans, amount)
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj 
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != 0 and ni * n + nj not in seen:
                    q.append(
                        (ni, nj, amount + grid[ni][nj], seen | set([ni * n + nj, ]) )
                    )

        return ans

