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

