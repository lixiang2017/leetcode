'''
in-place

state rules/table:
0: die -> die
1: live -> live
2: live -> die
3: die -> live

ref:
https://www.cnblogs.com/grandyang/p/4854466.html

You are here!
Your runtime beats 99.20 % of python submissions.

22 / 22 test cases passed.
    Status: Accepted
Runtime: 12 ms
Memory Usage: 13.6 MB
    
Submitted: 0 minutes ago
'''

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:  return []
        if not board[0]: return [[]]
        
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                # count lives
                lives = 0
                deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                for x_delta, y_delta in deltas:
                    x, y = i + x_delta, j + y_delta
                    if 0 <= x < m and 0 <= y < n and (1 == board[x][y] or 2 == board[x][y]):
                        lives += 1
                # print 'lives: ', lives
                if 1 == board[i][j] or 2 == board[i][j]:    
                    if lives < 2 or lives > 3:
                        board[i][j] = 2
                else:
                    if lives == 3:
                        board[i][j] = 3                  
        
        for i in range(m):
            for j in range(n):
                board[i][j] %= 2
    
    