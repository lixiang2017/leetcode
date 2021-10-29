'''
BFS

429 mstime cost
·
13.27 MBmemory cost
·
Your submission beats87.80 %Submissions
'''
from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        # write your code here
        M, N = len(rooms), len(rooms[0])
        zero = deque()
        for i in range(M):
            for j in range(N):
                if rooms[i][j] == 0:
                    zero.append((i, j))
        while zero:
            i, j = zero.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N:
                    if rooms[ni][nj] != -1 and (rooms[i][j] + 1 < rooms[ni][nj]):
                        rooms[ni][nj] = rooms[i][j] + 1
                        zero.append((ni, nj))
