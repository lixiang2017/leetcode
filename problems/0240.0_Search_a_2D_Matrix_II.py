'''
T: O(MN)
S: O(1)

Runtime: 352 ms, faster than 11.71% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.4 MB, less than 40.22% of Python3 online submissions for Search a 2D Matrix II.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i, row in enumerate(matrix):
            for j, x in enumerate(row):
                if x == target:
                    return True
        return False


'''
from top-right to bottom-left
T: O(M + N)
S: O(1)

Runtime: 299 ms, faster than 32.80% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.5 MB, less than 40.22% of Python3 online submissions for Search a 2D Matrix II.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) if matrix else 0 
        i, j = 0, n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True 
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

'''
from bottom-left to top-right
T: O(M + N)
S: O(1)

Runtime: 398 ms, faster than 5.12% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage: 20.3 MB, less than 84.45% of Python3 online submissions for Search a 2D Matrix II.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) if matrix else 0 
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True 
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False


