'''
BFS

执行用时：44 ms, 在所有 Python3 提交中击败了95.48% 的用户
内存消耗：16.1 MB, 在所有 Python3 提交中击败了70.34% 的用户
通过测试用例：52 / 52
'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0
        if k >= m + n - 3:
            return m + n - 2
        
        visited = set([0, 0, k])
        q = deque([(0, 0, k)])
        step = 0
        while q:
            step += 1
            for _ in range(len(q)):
                x, y, rest = q.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy 
                    if 0 <= nx < m and 0 <= ny < n:
                        if grid[nx][ny] == 0 and (nx, ny, rest) not in visited:
                            if nx == m - 1 and ny == n - 1:
                                return step 
                            q.append((nx, ny, rest))
                            visited.add((nx, ny, rest))
                        elif grid[nx][ny] == 1 and rest > 0 and (nx, ny, rest - 1) not in visited:
                            q.append((nx, ny, rest - 1))
                            visited.add((nx, ny, rest - 1))
        return -1
