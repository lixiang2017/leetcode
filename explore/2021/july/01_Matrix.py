'''
BFS
Time: O(2MN)
Space: O(3MN)

You are here!
Your runtime beats 33.98 % of python3 submissions.
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        M, N = len(mat), len(mat[0])
        q = deque()
        seen = set()
        update = copy.deepcopy(mat)
        for i in range(M):
            for j in range(N):
                if 0 == mat[i][j]:
                    q.append((i, j, mat[i][j]))
                    seen.add((i, j))
                else:
                    update[i][j] = 20005
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            i, j, e = q.popleft()
            for deltax, deltay in directions:
                ni, nj = i + deltax, j + deltay
                if 0 <= ni < M and 0 <= nj < N and (ni, nj) not in seen:
                    update[ni][nj] = min(update[ni][nj], e + 1)
                    q.append((ni, nj, update[ni][nj]))
                    seen.add((ni, nj))
        
        return update
