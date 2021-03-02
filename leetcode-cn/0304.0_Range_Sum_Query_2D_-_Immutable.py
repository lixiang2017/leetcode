'''
approach: 2D Prefix Sum
Time: O(M * N) for __init__, and O(1) for sumRegion
Space: O(M * N)

执行用时：152 ms, 在所有 Python 提交中击败了74.36%的用户
内存消耗：15.9 MB, 在所有 Python 提交中击败了58.97%的用户
'''


class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # [i][j] -> preSum[i+1][j+1]
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        self.preSum = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                self.preSum[i + 1][j + 1] = \
                    self.preSum[i + 1][j] + self.preSum[i][j + 1] \
                    - self.preSum[i][j] + matrix[i][j]
     

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.preSum[row2 + 1][col2 + 1] - self.preSum[row1][col2 + 1] - \
            self.preSum[row2 + 1][col1] + self.preSum[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

'''
        # print preSum
        for i in range(M + 1):
            print self.preSum[i] 
[0, 0, 0, 0, 0, 0]
[0, 3, 3, 4, 8, 10]
[0, 8, 14, 18, 24, 27]
[0, 9, 17, 21, 28, 36]
[0, 13, 22, 26, 34, 49]
[0, 14, 23, 30, 38, 58]
'''

'''
执行出错信息：
Line 8: IndexError: list index out of range
最后执行的输入：
["NumMatrix"]
[[[]]]
# solution:
M, N = len(matrix), len(matrix[0]) if matrix else 0
'''

