'''
DFS / backtracking

Success
Details 
Runtime: 388 ms, faster than 33.06% of Python online submissions for Word Search.
Memory Usage: 17.8 MB, less than 47.23% of Python online submissions for Word Search.

ref:
https://leetcode.com/problems/word-search/discuss/1004342/Python-Simple-Solution-or-DFS
'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, word, i, j): return True
        return False
    
    def dfs(self, board, word, i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]): return False
        if board[i][j] == -1 or board[i][j] != word[0]: return False
        if len(word) == 1: return True
        
        takeout, board[i][j] = board[i][j], -1
        if self.dfs(board, word[1:], i + 1, j): return True
        if self.dfs(board, word[1:], i - 1, j): return True
        if self.dfs(board, word[1:], i, j + 1): return True
        if self.dfs(board, word[1:], i, j - 1): return True
        board[i][j] = takeout
        
