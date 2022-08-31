'''
BFS

Runtime: 539 ms, faster than 28.91% of Python3 online submissions for Pacific Atlantic Water Flow.
Memory Usage: 15.6 MB, less than 55.20% of Python3 online submissions for Pacific Atlantic Water Flow.
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        # reach p, a 
        p = [[1] * n] + [[1] + [0] * (n- 1) for _ in range(m - 1)]
        a = [([0] * (n - 1) + [1]) for _ in range(m - 1)] + [[1] * n]
        
        def bfs(matrix):
            q = deque()
            seen = set()
            for i in range(m):
                for j in range(n):     
                    if 1 == matrix[i][j]:
                        q.append([i, j])
                        seen.add(i * n + j)
            while q:
                i, j = q.popleft()
                for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                    if 0 <= ni < m and 0 <= nj < n and ni * n + nj not in seen and heights[ni][nj] >= heights[i][j]:
                        q.append([ni, nj])
                        seen.add(ni * n + nj)
                        matrix[ni][nj] = 1
                        
        bfs(p)
        bfs(a)
        
        ans = []
        for i in range(m):
            for j in range(n):
                if p[i][j] and a[i][j]:
                    ans.append([i, j])
        return ans 
