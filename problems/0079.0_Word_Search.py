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



'''
DFS

Runtime: 8792 ms, faster than 11.32% of Python3 online submissions for Word Search.
Memory Usage: 14.4 MB, less than 11.68% of Python3 online submissions for Word Search.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M, N, L = len(board), len(board[0]), len(word)
        
        def dfs(i, j, seen, idx):
            if idx == L:
                return True            
            if board[i][j] != word[idx] or (i, j) in seen:
                return False
            if idx == L - 1:
                return True
            
            seen.add((i, j))
            ans = False
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = di + i, dj + j
                if 0 <= ni < M and 0 <= nj < N:
                    # need to use seen.copy()
                    ans |= dfs(ni, nj, seen.copy(), idx + 1)
            return ans
        
        # driver
        for x in range(M):
            for y in range(N):
                if dfs(x, y, set(), 0):
                    return True
        return False

'''
Input
[["a"]]
"a"
Output
false
Expected
true


Input: [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
"ABCESEEEFS"
Output: false
Expected: true
'''

