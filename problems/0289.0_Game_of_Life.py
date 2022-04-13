'''
Runtime: 77 ms, faster than 5.32% of Python3 online submissions for Game of Life.
Memory Usage: 13.9 MB, less than 93.38% of Python3 online submissions for Game of Life.
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0]) if board else 0
        for i in range(m):
            for j in range(n):
                cnt = 0
                for ii in range(max(i - 1, 0), min(i + 2, m)):
                    for jj in range(max(j - 1, 0), min(j + 2, n)):
                        if (i == ii and j == jj):
                            continue
                        if board[ii][jj] & 1:
                            cnt += 1
                if cnt == 3 or (board[i][j] and cnt == 2):
                    board[i][j] += 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1


'''
Runtime: 51 ms, faster than 40.04% of Python3 online submissions for Game of Life.
Memory Usage: 13.9 MB, less than 93.38% of Python3 online submissions for Game of Life.
'''
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0]) if board else 0
        for i in range(m):
            for j in range(n):
                cnt = 0
                for ii in range(max(i - 1, 0), min(i + 2, m)):
                    for jj in range(max(j - 1, 0), min(j + 2, n)):
                        if board[ii][jj] & 1 and not (i == ii and j == jj):
                            cnt += 1
                if cnt == 3 or (board[i][j] and cnt == 2):
                    board[i][j] += 2
        
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1


