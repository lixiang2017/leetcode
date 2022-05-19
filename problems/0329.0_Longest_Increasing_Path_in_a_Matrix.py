'''
BFS

Runtime: 3753 ms, faster than 5.02% of Python3 online submissions for Longest Increasing Path in a Matrix.
Memory Usage: 15.4 MB, less than 64.65% of Python3 online submissions for Longest Increasing Path in a Matrix.
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        ans = 1
        path = [[1] * n for _ in range(m)]
        # (i, j, 1)
        q = deque([(i, j, 1) for i in range(m) for j in range(n)])
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            i, j, p = q.popleft()
            for di, dj in DIR:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j] and path[ni][nj] < path[i][j] + 1:
                    path[ni][nj] = path[i][j] + 1
                    q.append((ni, nj, path[ni][nj]))
                    ans = max(ans, path[ni][nj])
                    
        return ans 
        

'''
先把自己周围的都算出来，最后再算自己
DFS + memoization

Runtime: 668 ms, faster than 40.68% of Python3 online submissions for Longest Increasing Path in a Matrix.
Memory Usage: 15 MB, less than 74.04% of Python3 online submissions for Longest Increasing Path in a Matrix.
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        path = [[1] * n for _ in range(m)]
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if path[i][j] != 1:
                return path[i][j]
            for di, dj in DIR:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                    path[i][j] = max(path[i][j], dfs(ni, nj) + 1)
            return path[i][j]
            
        for i in range(m):
            for j in range(n):
                path[i][j] = dfs(i, j)
        return max(chain(*path))


'''
ans = max(ans, path[i][j])

Runtime: 573 ms, faster than 59.15% of Python3 online submissions for Longest Increasing Path in a Matrix.
Memory Usage: 14.8 MB, less than 85.91% of Python3 online submissions for Longest Increasing Path in a Matrix.
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        path = [[1] * n for _ in range(m)]
        DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            if path[i][j] != 1:
                return path[i][j]
            for di, dj in DIR:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] < matrix[i][j]:
                    path[i][j] = max(path[i][j], dfs(ni, nj) + 1)
            return path[i][j]
        
        ans = 0
        for i in range(m):
            for j in range(n):
                path[i][j] = dfs(i, j)
                ans = max(ans, path[i][j])
        return ans 



