'''
计算每块 island 对周长的贡献。
周围四个方块，最多可贡献值为4。对于每一个方向，如果到达边界或者为 water，即可贡献 1.


Runtime: 609 ms, faster than 51.59% of Python3 online submissions for Island Perimeter.
Memory Usage: 14.6 MB, less than 61.43% of Python3 online submissions for Island Perimeter.
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def cycle(x, y):
            if 0 == grid[x][y]:
                return 0
            p = 0
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if nx < 0 or nx >= r or ny < 0 or ny >= c or grid[nx][ny] == 0:
                    p += 1
            return p
        
        peri = 0
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                peri += cycle(i, j)
        return peri


'''
Runtime: 724 ms, faster than 28.09% of Python3 online submissions for Island Perimeter.
Memory Usage: 14.7 MB, less than 61.43% of Python3 online submissions for Island Perimeter.
'''
from itertools import chain
from operator import ne
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return sum(sum(map(ne, chain([0], row), chain(row,[0]))) for row in chain(grid, zip(*grid)))


'''
Runtime: 530 ms, faster than 65.89% of Python3 online submissions for Island Perimeter.
Memory Usage: 14.5 MB, less than 81.31% of Python3 online submissions for Island Perimeter.
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        area = 0
        for row in grid + list(map(list, zip(*grid))):
            for i1, i2 in zip([0] + row, row + [0]):
                area += int(i1 != i2)
        return area

'''
DFS

Runtime: 817 ms, faster than 18.35% of Python3 online submissions for Island Perimeter.
Memory Usage: 18.6 MB, less than 13.82% of Python3 online submissions for Island Perimeter.
'''
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not len(grid) or not len(grid[0]):
            return 0
        # visited
        seen = set()
        # iteration
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (i, j) not in seen:
                    ans = self.dfs(grid, i, j, seen)
                    break
        return ans
    
    def dfs(self, grid, i, j, seen):
        # if boundary, return 1 and stop exploring
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 1
        # if 0, return 1 and stop exploring
        if not grid[i][j]:
            return 1
        # if visited, stop exploring
        if (i, j) in seen:
            return 0
        seen.add((i, j))
        up = self.dfs(grid, i - 1, j, seen)
        down = self.dfs(grid, i + 1, j, seen)
        left = self.dfs(grid, i, j - 1, seen)
        right = self.dfs(grid, i, j + 1, seen)
        return up + down + left + right
    
