'''
# not in-place

You are here!
Your runtime beats 37.53 % of python submissions.
You are here!
Your memory usage beats 95.54 % of python submissions.
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return []
        m = len(board)
        n = len(board[0])
        new_board = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # count lives
                lives = 0
                deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                for x_delta, y_delta in deltas:
                    x, y = i + x_delta, j + y_delta
                    if 0 <= x < m and 0 <= y < n and 1 == board[x][y]:
                        lives += 1
                # print 'lives: ', lives
                if 1 == board[i][j]:    
                    if lives in (2, 3):
                        new_board[i][j] = 1
                else:
                    if lives == 3:
                        new_board[i][j] = 1                    
        #borad = new_board
        #return new_board
        for i in range(m):
            for j in range(n):
                board[i][j] = new_board[i][j]
    
    