'''
approach: backtracking

You are here!
Your runtime beats 26.80 % of python3 submissions.
You are here!
Your memory usage beats 86.25 % of python3 submissions.
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.pos = [-1] * n
        self.ans = []
        self.backtracking(0, n)
        return self.ans
    
    def isValid(self, row):
        for j in range(row):
            if self.pos[j] == self.pos[row] or row - j == abs(self.pos[row] - self.pos[j]):
                return False
        return True
    
    def backtracking(self, row, N):
        if row == N:
            chessboard = []
            for p in self.pos:
                one_row = ['.'] * N
                one_row[p] = 'Q'
                chessboard.append(''.join(one_row))
            self.ans.append(chessboard)
            return
        
        for col in range(N):
            self.pos[row] = col
            if self.isValid(row):
                self.backtracking(row + 1, N)
            
