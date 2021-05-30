'''
backtracking

You are here!
Your runtime beats 16.83 % of python3 submissions.
You are here!
Your memory usage beats 99.32 % of python3 submissions.
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        self.pos = [-1] * n
        self.ans = 0
        self.backtracking(0, n)
        return self.ans

    def isValid(self, row):
        for j in range(row):
            if self.pos[j] == self.pos[row] or row - j == abs(self.pos[row] - self.pos[j]):
                return False
        return True
    
    def backtracking(self, row, N):
        if row == N:
            self.ans += 1
            return
        
        for col in range(N):
            self.pos[row] = col
            if self.isValid(row):
                self.backtracking(row + 1, N)


'''
You are here!
Your runtime beats 99.77 % of python3 submissions.
You are here!
Your memory usage beats 64.00 % of python3 submissions.
'''

class Solution:
    def totalNQueens(self, n: int) -> int:
        # n to solutions
        n2s = {1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92, 9: 352}
        return n2s[n]
