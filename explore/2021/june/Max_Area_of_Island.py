'''
DFS
T: O(MN)
S: O(MN)
'''
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        M, N = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.visited = [[False] * N for _ in range(M)]
        
        def dfs(x, y):
            if (not self.withinArea(x, y, M, N)) or self.visited[x][y] or 1 != grid[x][y]:
                return 0
            self.visited[x][y] = True
            grid[x][y] = 0
            area = 1
            for deltax, deltay in directions:
                nx, ny = x + deltax, y + deltay
                area += dfs(nx, ny)
            return area
        
        for i in range(M):
            for j in range(N):
                if 1 == grid[i][j]:
                    max_area = max(max_area, dfs(i, j))

        return max_area

    
    def withinArea(self, x, y, M, N):
        return 0 <= x < M and 0 <= y < N
    