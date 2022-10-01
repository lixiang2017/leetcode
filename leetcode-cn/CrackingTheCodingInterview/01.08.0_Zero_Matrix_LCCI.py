'''
额外使用两个变量
T: O(3MN), S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了70.22% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了50.14% 的用户
通过测试用例：159 / 159
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # check
        isFirstRowZero = isFirstColumnZero = False 
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == 0:
                    if i == 0:
                        isFirstRowZero = True 
                    if j == 0:
                        isFirstColumnZero = True 
                    matrix[0][j] = 0
                    matrix[i][0] = 0 
        # set
        m, n = len(matrix), len(matrix[0]) if matrix else 0 
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        if isFirstRowZero:
            matrix[0] = [0] * n 
        if isFirstColumnZero:
            for i in range(m):
                matrix[i][0] = 0 


'''
额外使用两个变量
T: O(2MN), S: O(1)

执行用时：44 ms, 在所有 Python3 提交中击败了70.22% 的用户
内存消耗：15.4 MB, 在所有 Python3 提交中击败了84.09% 的用户
通过测试用例：159 / 159
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # check
        m, n = len(matrix), len(matrix[0]) if matrix else 0        
        isFirstRowZero = isFirstColumnZero = False 
        for j in range(n):
            if matrix[0][j] == 0:
                isFirstRowZero = True 
                break
        for i in range(m):
            if matrix[i][0] == 0:
                isFirstColumnZero = True 
                break
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][j]:
                    matrix[0][j] = 0
                    matrix[i][0] = 0 
        # set
        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if isFirstRowZero:
            matrix[0] = [0] * n 
        if isFirstColumnZero:
            for i in range(m):
                matrix[i][0] = 0 

'''
额外仅使用一个变量
T: O(2MN), S: O(1)

执行用时：40 ms, 在所有 Python3 提交中击败了87.02% 的用户
内存消耗：15.5 MB, 在所有 Python3 提交中击败了42.21% 的用户
通过测试用例：159 / 159
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # check
        m, n = len(matrix), len(matrix[0]) if matrix else 0        
        isFirstColumn0 = False 
        # top-left element matrix[0][0] marks the first row
        for i in range(m):
            if matrix[i][0] == 0:
                isFirstColumn0 = True
            for j in range(1, n):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        # set
        for i in range(m - 1, -1, -1):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
            if isFirstColumn0:
                matrix[i][0] = 0

