'''
BFS

Runtime: 48 ms, faster than 91.88% of Python3 online submissions for Rotting Oranges.
Memory Usage: 14.3 MB, less than 68.53% of Python3 online submissions for Rotting Oranges.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        one, two = 0, deque()
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if 1 == grid[i][j]:
                    one += 1
                elif 2 == grid[i][j]:
                    two.append([i, j])
        step = 0
        while two and (one != 0):
            next_two = deque()
            for _ in range(len(two)):
                i, j = two.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        one -= 1
                        next_two.append((ni, nj))
                grid[i][j] = 3
            step += 1
            two = next_two
        
        return [-1, step][one == 0]


'''
BFS, no need to use next_two

Runtime: 44 ms, faster than 97.47% of Python3 online submissions for Rotting Oranges.
Memory Usage: 14.3 MB, less than 68.53% of Python3 online submissions for Rotting Oranges.
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        one, two = 0, deque()
        M, N = len(grid), len(grid[0])
        for i in range(M):
            for j in range(N):
                if 1 == grid[i][j]:
                    one += 1
                elif 2 == grid[i][j]:
                    two.append([i, j])
        step = 0
        while two and (one != 0):
            for _ in range(len(two)):
                i, j = two.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        one -= 1
                        two.append((ni, nj))
                grid[i][j] = 3
            step += 1
        
        return [-1, step][one == 0]

