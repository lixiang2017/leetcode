'''
DFS

Runtime: 132 ms, faster than 92.68% of Python3 online submissions for Surrounded Regions.
Memory Usage: 16.2 MB, less than 41.21% of Python3 online submissions for Surrounded Regions.
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])
        
        # infect function
        def dfs(board, x, y):
            if x < 0 or x >= M or y < 0 or y >= N or board[x][y] != 'O':
                return
            # change board 'O' to 'B'
            board[x][y] = 'B'
            dfs(board, x - 1, y)
            dfs(board, x + 1, y)
            dfs(board, x, y + 1)
            dfs(board, x, y - 1)
        
        # to find 'O' on the board
        ## left and right, change 'O' to 'B'
        for i in range(M):
            dfs(board, i, 0)
            dfs(board, i, N - 1)
        ## top and bottom
        for j in range(1, N - 1):
            dfs(board, 0, j)
            dfs(board, M - 1, j)
        
        # recover 'B' to 'O', change 'O' to 'X'
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'



'''
BFS

Runtime: 124 ms, faster than 99.41% of Python3 online submissions for Surrounded Regions.
Memory Usage: 15.5 MB, less than 91.43% of Python3 online submissions for Surrounded Regions.
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M, N = len(board), len(board[0])        
        # to find 'O' on the board
        ## left and right, change 'O' to 'B'
        q = deque()
        for i in range(M):
            for j in [0, N - 1]:
                if board[i][j] == 'O':
                    board[i][j] = 'B'
                    q.append([i, j])
        ## top and bottom
        for j in range(1, N - 1):
            for i in [0, M - 1]:
                if board[i][j] == 'O':
                    board[i][j] = 'B'
                    q.append([i, j])                
        
        while q:
            i, j = q.popleft()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and board[ni][nj] == 'O':
                    board[ni][nj] = 'B'
                    q.append([ni, nj])
        
        # recover 'B' to 'O', change 'O' to 'X'
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

