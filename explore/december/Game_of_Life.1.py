'''
in place
bitwise: xx: the left bit means the next state, the right bit means the current state

Time: O(M * N)
Space: O(1)

You are here!
Your runtime beats 91.34 % of python submissions.
You are here!
Your memory usage beats 44.88 % of python submissions.
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:  return []
        if not board[0]: return [[]]
        
        m, n = len(board), len(board[0])
        deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        # add left bit
        for i in range(m):
            for j in range(n):
                lives = 0
                for x_delta, y_delta in deltas:
                    x, y = i + x_delta, j + y_delta
                    if 0 <= x < m and 0 <= y < n and board[x][y] & 1:
                        lives += 1
                
                if board[i][j] & 1:
                    if lives in (2, 3):
                        board[i][j] += 2
                else:
                    if lives == 3:
                        board[i][j] += 2
                
        # remove right bit
        for i in range(m):
            for j in range(n):
                board[i][j] >>= 1
                