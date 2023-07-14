'''
DP
T: O(N^2)
S: O(1)

执行用时：64 ms, 在所有 Python3 提交中击败了70.64% 的用户
内存消耗：16.8 MB, 在所有 Python3 提交中击败了69.92% 的用户
通过测试用例：50 / 50
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if 1 == n:
            return matrix[0][0]

        for i in range(1, n):
            for j in range(n):
                matrix[i][j] += min(
                    matrix[i - 1][j - 1] if j > 0 else inf,
                    matrix[i - 1][j],
                    matrix[i - 1][j + 1] if j + 1 < n else inf
                )
        return min(matrix[-1])
