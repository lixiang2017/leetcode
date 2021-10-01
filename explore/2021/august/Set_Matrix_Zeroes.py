'''
Time: O(2MN)
Space: O(1)

You are here!
Your runtime beats 71.68 % of python3 submissions.
You are here!
Your memory usage beats 74.68 % of python3 submissions.
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0])
        # first row, set zeros or not
        first = False
        for j in range(N):
            if 0 == matrix[0][j]:
                first = True
                break
        
        # row, column, get
        for i in range(1, M):
            for j in range(N):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # set row and column
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # first column
        if 0 == matrix[0][0]:
            for i in range(M):
                matrix[i][0] = 0
        # first row
        if first:
            for j in range(N):
                matrix[0][j] = 0 
        