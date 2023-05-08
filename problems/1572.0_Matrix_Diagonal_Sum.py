'''
Runtime: 128 ms, faster than 5.85% of Python3 online submissions for Matrix Diagonal Sum.
Memory Usage: 16.6 MB, less than 11.57% of Python3 online submissions for Matrix Diagonal Sum.
'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        ans = sum(mat[i][i] + mat[i][n - 1 - i] for i in range(n))
        if n % 2:
            ans -= mat[n // 2][n // 2]
        return ans 
        