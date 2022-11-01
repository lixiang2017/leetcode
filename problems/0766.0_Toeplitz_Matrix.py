'''
Runtime: 92 ms, faster than 91.65% of Python3 online submissions for Toeplitz Matrix.
Memory Usage: 13.9 MB, less than 36.74% of Python3 online submissions for Toeplitz Matrix.
'''
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] != matrix[r - 1][c - 1]:
                    return False
        return True
        
        