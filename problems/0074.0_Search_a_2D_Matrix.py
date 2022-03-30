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
