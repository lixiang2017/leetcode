'''
__init__
T: O(MN)
S: O(MN)

sumRegion
T: O(1)
S: O(1)

Runtime: 2441 ms, faster than 34.41% of Python3 online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 24.7 MB, less than 89.51% of Python3 online submissions for Range Sum Query 2D - Immutable.
'''
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        self.pre = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.pre[i][j] = matrix[i][j]
                if i > 0:
                    self.pre[i][j] += self.pre[i - 1][j]
                if j > 0:
                    self.pre[i][j] += self.pre[i][j - 1]
                if i > 0 and j > 0:
                    self.pre[i][j] -= self.pre[i - 1][j - 1] 
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.pre[row2][col2]
        if col1 > 0:
            s -= self.pre[row2][col1 - 1]
        if row1 > 0:
            s -= self.pre[row1 - 1][col2]
        if row1 > 0 and col1 > 0:
            s += self.pre[row1 - 1][col1 - 1]
        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

'''
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[-4,-5]]],[0,0,0,0],[0,0,0,1],[0,1,0,1]]
'''



'''
change to (m + 1) * (n + 1)
__init__
T: O(MN)
S: O(MN)

sumRegion
T: O(1)
S: O(1)


Runtime: 2312 ms, faster than 40.18% of Python3 online submissions for Range Sum Query 2D - Immutable.
Memory Usage: 24.8 MB, less than 69.33% of Python3 online submissions for Range Sum Query 2D - Immutable.
'''
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        self.pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.pre[i][j] = matrix[i - 1][j - 1] \
                    + self.pre[i - 1][j] + self.pre[i][j - 1] \
                    - self.pre[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre[row2 + 1][col2 + 1] \
            - self.pre[row2 + 1][col1] - self.pre[row1][col2 + 1] \
            + self.pre[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


