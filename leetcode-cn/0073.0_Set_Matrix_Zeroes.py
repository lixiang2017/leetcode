'''
Time: O(M * N * 2) = O(MN)
Space: O(M + N)

执行用时：20 ms, 在所有 Python 提交中击败了99.38%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了27.02%的用户
'''


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        row, column = [False] * M, [False] * N
        for i in range(M):
            for j in range(N):
                if 0 == matrix[i][j]:
                    row[i] = column[j] = True
        
        for i in range(M):
            for j in range(N):
                if row[i] or column[j]:
                    matrix[i][j] = 0



'''
Time: O(M * N * 2 + 2 * M + 2 * N) = O(MN)
Space: O(1)

执行用时：40 ms, 在所有 Python 提交中击败了28.26的用户
内存消耗：13.9 MB, 在所有 Python 提交中击败了8.69%的用户
'''

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        flag_row0 = any(matrix[i][0] == 0 for i in range(M))
        flag_col0 = any(matrix[0][j] == 0 for j in range(N))

        for i in range(1, M):
            for j in range(1, N):
                if 0 == matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if flag_row0:
            for i in range(M):
                matrix[i][0] = 0
        if flag_col0:
            for j in range(N):
                matrix[0][j] = 0



'''
Time: O(MN)
Space: O(1)

执行用时：28 ms, 在所有 Python 提交中击败了83.85%的用户
内存消耗：13.7 MB, 在所有 Python 提交中击败了38.82%的用户
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        M, N = len(matrix), len(matrix[0]) if matrix else 0
        flag_row0 = False

        for i in range(M):
            if matrix[i][0] == 0:
                flag_row0 = True
            for j in range(1, N):   # range(N) will be wrong
                if 0 == matrix[i][j]:
                    matrix[i][0] = matrix[0][j] = 0
        
        for i in range(M - 1, -1, -1):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if flag_row0:
                matrix[i][0] = 0
        

