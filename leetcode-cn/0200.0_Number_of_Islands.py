'''
BFS

执行用时：156 ms, 在所有 Python3 提交中击败了16.75% 的用户
内存消耗：28.6 MB, 在所有 Python3 提交中击败了5.00% 的用户
通过测试用例：49 / 49
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0]) if grid else 0
        seen, ans = set(), 0
        for i in range(m):
            for j in range(n):
                if (i, j) in seen or grid[i][j] == '0':
                    continue
                ans += 1
                seen.add((i, j))
                q = deque([(i, j), ])
                while q:
                    ii, jj = q.popleft()
                    for ni, nj in [(ii-1, jj), (ii+1, jj), (ii, jj-1), (ii, jj+1)]:
                        if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen and grid[ni][nj] == '1':
                            q.append((ni, nj))
                            seen.add((ni, nj))

        return ans

