'''
BFS

执行用时：280 ms, 在所有 Python3 提交中击败了60.79% 的用户
内存消耗：19 MB, 在所有 Python3 提交中击败了7.54% 的用户
通过测试用例：50 / 50
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0]) if mat else 0
        dist = [[m + n] * n for _ in range(m)]
        q, seen = deque(), set()
        for i in range(m):
            for j in range(n):
                if 0 == mat[i][j]:
                    dist[i][j] = 0
                    q.append((i, j))
                    seen.add((i, j))

        while q:
            i, j = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj 
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen and dist[ni][nj] > dist[i][j] + 1:
                    dist[ni][nj] = dist[i][j] + 1
                    q.append((ni, nj))
                    seen.add((ni, nj))

        return dist 

