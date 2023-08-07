'''
binary search
T: O(log(MN))
S: O(1)

Runtime: 48 ms, faster than 84.58% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 14.5 MB, less than 46.15% of Python3 online submissions for Search a 2D Matrix.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0]) if matrix else 0
        i, j = 0, m * n - 1
        while i <= j:
            mid = (i + j) // 2
            x, y = divmod(mid, n)
            if target == matrix[x][y]:
                return True
            elif target > matrix[x][y]:
                i = mid + 1
            else:
                j = mid - 1
        return False

'''
binary search
T: O(log(MN))
S: O(1)

Runtime: 54 ms, faster than 76.18% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 16.8 MB, less than 64.57% of Python3 online submissions for Search a 2D Matrix.
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            i, j = divmod(mid, n)
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
