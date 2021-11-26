'''
DFS

执行用时：60 ms, 在所有 Python3 提交中击败了87.93% 的用户
内存消耗：17.9 MB, 在所有 Python3 提交中击败了29.05% 的用户
通过测试用例：728 / 728
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # 九坤投资，一面技术面面试题  2021/11/23 22:15   
        matrix = grid
        m, n = len(matrix), len(matrix[0])
        ans = 0

        def dfs(x, y):
            a = 1
            matrix[x][y] = 2
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if matrix[nx][ny] == 1:
                        a += dfs(nx, ny)
            return a 

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    area = dfs(i, j)
                    ans = max(ans, area)

        return ans


'''
BFS

执行用时：64 ms, 在所有 Python3 提交中击败了78.58% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了81.41% 的用户
通过测试用例：728 / 728
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if 1 == grid[i][j]:
                    a = 1
                    grid[i][j] = 2
                    q = deque([(i, j)])
                    while q:
                        x, y = q.popleft()
                        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < m and 0 <= ny < n:
                                if grid[nx][ny] == 1:
                                    grid[nx][ny] = 2
                                    a += 1
                                    q.append((nx, ny))

                    ans = max(ans, a)

        return ans

'''
Union Find

执行用时：116 ms, 在所有 Python3 提交中击败了7.23% 的用户
内存消耗：15.2 MB, 在所有 Python3 提交中击败了76.91% 的用户
通过测试用例：728 / 728
'''
class UF:
    def __init__(self, n):
        self.p = list(range(n))
    def find(self, x):
        if x != self.p[x]:
            self.p[x] = self.find(self.p[x])
            x = self.p[x]
        return x
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.p[px] = py

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UF(m * n)
        for i in range(m):
            for j in range(n):
                if 1 == grid[i][j]:
                    for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and 1 == grid[ni][nj]:
                            uf.union(i * n + j, ni * n + nj)

        c = Counter(uf.find(i * n + j) for i in range(m) for j in range(n) if grid[i][j] == 1)
        return max(c.values()) if c else 0


