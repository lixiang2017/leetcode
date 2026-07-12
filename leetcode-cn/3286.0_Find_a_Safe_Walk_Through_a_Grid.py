class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dist = [[-inf] * n for _ in range(m)]
        dist[0][0] = health - grid[0][0]
        if dist[0][0] <= 0:
            return False

        q = deque([(0, 0, dist[0][0])])
        while q:
            i, j, h = q.popleft()
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and dist[x][y] < h - grid[x][y] > 0:
                    if x == m - 1 and y == n - 1:
                        return True
                    dist[x][y] = h - grid[x][y]
                    q.append((x, y, dist[x][y]))
        return False


"""appendleft"""


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dist = [[-inf] * n for _ in range(m)]
        dist[0][0] = health - grid[0][0]
        if dist[0][0] <= 0:
            return False

        q = deque([(0, 0)])
        while q:
            i, j = q.popleft()
            h = dist[i][j]
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n:
                    cost = grid[x][y]
                    if dist[x][y] < h - cost > 0:
                        if x == m - 1 and y == n - 1:
                            return True
                        dist[x][y] = h - cost
                        if cost == 0:
                            q.appendleft((x, y))
                        else:
                            q.append((x, y))
        return False
