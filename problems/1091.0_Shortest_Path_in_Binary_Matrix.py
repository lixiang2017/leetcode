'''
BFS

Runtime: 630 ms, faster than 86.36% of Python3 online submissions for Shortest Path in Binary Matrix.
Memory Usage: 15.4 MB, less than 26.25% of Python3 online submissions for Shortest Path in Binary Matrix.
'''
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0:
            return -1
        if n == 1:
            return 1 if grid[0][0] == 0 else -1
        # (x, y, step)
        q = deque([(0, 0, 1)])
        seen = set([(0, 0)])
        DIR = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while q:
            x, y, step = q.popleft()
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy 
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in seen and grid[nx][ny] == 0:
                    if nx == n - 1 and ny == n - 1:
                        return step + 1
                    q.append((nx, ny, step + 1))
                    seen.add((nx, ny))
        return -1
            
            
'''
Runtime: 749 ms, faster than 27.16% of Python3 online submissions for Shortest Path in Binary Matrix.
Memory Usage: 17.9 MB, less than 12.33% of Python3 online submissions for Shortest Path in Binary Matrix.
'''
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0:
            return -1
        elif grid == [[0]]:
            return 1
        seen = set([(0, 0)])
        # (x, y, length)
        q = deque([(0, 0, 1)])
        while q:
            x, y, _len = q.popleft()
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    nx, ny = x + dx, y + dy 
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0 and not (x == nx and y == ny)  and (nx, ny) not in seen:
                        if nx == n - 1 and ny == n - 1:
                            return _len + 1
                        seen.add((nx, ny))
                        q.append((nx, ny, _len + 1))
        
        return -1
        