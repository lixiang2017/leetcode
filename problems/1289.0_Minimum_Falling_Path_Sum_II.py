'''
DP

Runtime: 1365 ms, faster than 24.79% of Python3 online submissions for Minimum Falling Path Sum II.
Memory Usage: 18.3 MB, less than 27.27% of Python3 online submissions for Minimum Falling Path Sum II.
'''
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        matrix = grid
        n = len(matrix)
        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(matrix[i - 1][: j] + matrix[i - 1][j + 1:])
        return min(matrix[-1])

'''
Input
[[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]
Output
-67
Expected
-192
'''
