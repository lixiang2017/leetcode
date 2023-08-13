'''
时间 48 ms 击败 30.38%
内存 16.5 MB 击败 7.51%
'''
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, s = len(mat), 0
        for i in range(n):
            s += mat[i][i] + mat[i][n - 1 - i]
        if n & 1:
            s -= mat[n // 2][n // 2]
        return s 
