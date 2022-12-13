'''
DP
T: O(N^2)
S: O(1)

Runtime: 138 ms, faster than 93.48% of Python3 online submissions for Minimum Falling Path Sum.
Memory Usage: 14.8 MB, less than 64.34% of Python3 online submissions for Minimum Falling Path Sum.
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(matrix[i - 1][j - 1] if j >= 1 else inf,
                                    matrix[i - 1][j], 
                                    matrix[i - 1][j + 1] if j + 1 < n else inf)
        return min(matrix[-1])
        
