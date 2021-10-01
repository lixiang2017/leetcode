'''
approach: PrefixSum 2D
Time: O(1)
Space: O(MN)

You are here!
Your runtime beats 88.58 % of python3 submissions.
You are here!
Your memory usage beats 40.55 % of python3 submissions.
'''


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        self.presum = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M):
            for j in range(N):
                self.presum[i + 1][j + 1] = self.presum[i + 1][j] + self.presum[i][j + 1] \
                    - self.presum[i][j] + matrix[i][j]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2 + 1][col2 + 1] - self.presum[row1][col2 + 1] - self.presum[row2 + 1][col1] + self.presum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


'''
You are here!
Your runtime beats 15.86 % of python3 submissions.
You are here!
Your memory usage beats 95.56 % of python3 submissions.
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum([sum(self.matrix[row][col1: col2 + 1]) for row in range(row1, row2 + 1)])
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)



'''
You are here!
Your runtime beats 33.32 % of python3 submissions.
You are here!
Your memory usage beats 81.66 % of python3 submissions.
'''


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.__matrix = [[0] + list(accumulate(row)) for row in matrix]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return sum(self.__matrix[r][col2 + 1] - self.__matrix[r][col1] for r in range(row1, row2 + 1))


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)