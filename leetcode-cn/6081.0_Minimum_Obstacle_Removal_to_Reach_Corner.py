'''
01BFS, appendleft + append
01bfs维护一个双端队列，当边权为0时，使用push_front，当边权为1时，使用push_back.

执行用时：1388 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：36.6 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        remove = [[m + n] * n for _ in range(m)]
        if grid[0][0] == 0:
            remove[0][0] = 0
        else:
            remove[0][0] = 1
        q = deque([(0, 0, remove[0][0])])
        DIR = [(-1, 0), (1, 0), (0,  -1), (0, 1)]
        
        while q:
            x, y, r = q.popleft()
            if r >= remove[-1][-1]:
                continue
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy 
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == 0:
                        if remove[nx][ny] > r and remove[nx][ny] <= remove[-1][-1]:
                            q.appendleft((nx, ny, r))
                            remove[nx][ny] = r
                    else:
                        if remove[nx][ny] > r + 1 and remove[nx][ny] <= remove[-1][-1]:
                            q.append((nx, ny, r + 1))
                            remove[nx][ny] = r + 1

        return remove[-1][-1]


'''
01 BFS

执行用时：1508 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：37.2 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # distance
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = 0
        q = deque([(0, 0)])
        
        while q:
            x, y = q.popleft()
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < m and 0 <= ny < n:
                    g = grid[nx][ny]
                    if dist[nx][ny] > dist[x][y] + g:
                        dist[nx][ny] = dist[x][y] + g
                        if 0 == g:
                            q.appendleft((nx, ny))
                        else:
                            q.append((nx, ny))
        return dist[-1][-1]


'''
BFS + heapq

执行用时：2092 ms, 在所有 Python3 提交中击败了100.00% 的用户
内存消耗：37.2 MB, 在所有 Python3 提交中击败了100.00% 的用户
通过测试用例：54 / 54
'''
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # distance
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = 0
        # heap (dist, x, y)
        h = [(0, 0, 0)]
        
        while h:
            d, x, y = heappop(h)
            if dist[x][y] >= dist[-1][-1]:
                continue
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if 0 <= nx < m and 0 <= ny < n:
                    g = grid[nx][ny]
                    if dist[nx][ny] > dist[x][y] + g and dist[nx][ny] <= dist[-1][-1]:
                        dist[nx][ny] = dist[x][y] + g
                        heappush(h, (dist[nx][ny], nx, ny))
        return dist[-1][-1]





