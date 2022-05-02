'''
这一题最主要的还是需要 反向思维。无论 BFS 还是 DFS，都需要反向思维。

正向处理 复杂度会特别高。正向处理针对每一个点都需要BFS，最终复杂度是 O(2 * MN * MN) = 32 * 10^8

反向处理，仍需要记录能到达的集合，避免再次搜索。
'''

'''
BFS

执行用时：88 ms, 在所有 Python3 提交中击败了74.26% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了66.17% 的用户
通过测试用例：113 / 113
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0]) if heights else 0
        ans = []
        canToPacific = [[False] * n for _ in range(m)]
        canToAtlantic = [[False] * n for _ in range(m)]
        # pacific
        p, seen = deque(), set()
        for j in range(n):
            canToPacific[0][j] = True
            p.append((0, j))
            seen.add((0, j))
        for i in range(1, m):
            canToPacific[i][0] = True
            p.append((i, 0))
            seen.add((i, 0))
        while p:
            i, j = p.popleft()
            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen and heights[i][j] <= heights[ii][jj]:
                    canToPacific[ii][jj] = True 
                    seen.add((ii, jj))
                    p.append((ii, jj))
        # atlantic
        a, seen = deque(), set()
        for j in range(n):
            canToAtlantic[m - 1][j] = True
            a.append((m - 1, j))
            seen.add((m - 1, j))
        for i in range(m - 1):
            canToAtlantic[i][n - 1] = True
            a.append((i, n - 1))
            seen.add((i, n - 1))
        while a:
            i, j = a.popleft()
            for ii, jj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen and heights[i][j] <= heights[ii][jj]:            
                    canToAtlantic[ii][jj] = True 
                    seen.add((ii, jj))
                    a.append((ii, jj))

        for i in range(m):
            for j in range(n):
                if canToPacific[i][j] and canToAtlantic[i][j]:
                    ans.append([i, j])
        return ans 

'''
DFS

执行用时：88 ms, 在所有 Python3 提交中击败了73.86% 的用户
内存消耗：19.4 MB, 在所有 Python3 提交中击败了5.22% 的用户
通过测试用例：113 / 113
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0]) if heights else 0

        def search(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set()
            def dfs(x: int, y: int):
                if (x, y) in visited:
                    return 
                visited.add((x, y))
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny)
            for x, y in starts:
                dfs(x, y)
            return visited 
        
        pacific = [(0, j) for j in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, search(pacific) & search(atlantic)))


'''
BFS

执行用时：104 ms, 在所有 Python3 提交中击败了47.24% 的用户
内存消耗：16.4 MB, 在所有 Python3 提交中击败了60.93% 的用户
通过测试用例：113 / 113
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0]) if heights else 0

        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            q = deque(starts)
            visited = set(starts)
            while q:
                x, y = q.popleft()
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
            return visited 
        
        pacific = [(0, j) for j in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, bfs(pacific) & bfs(atlantic)))


'''
执行用时：80 ms, 在所有 Python3 提交中击败了86.50% 的用户
内存消耗：16.2 MB, 在所有 Python3 提交中击败了86.69% 的用户
通过测试用例：113 / 113
'''
'''
turn directions into one dimension
0, 1
1, 0
0, -1
-1, 0

-> [0, 1, 0, -1, 0]
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0]) if heights else 0
        d = [0, 1, 0, -1, 0]

        def bfs(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            q = deque(starts)
            visited = set(starts)
            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx, ny = x + d[i], y + d[i + 1]
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in visited:
                        q.append((nx, ny))
                        visited.add((nx, ny))
            return visited 
        
        pacific = [(0, j) for j in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, j) for j in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, bfs(pacific) & bfs(atlantic)))


        
