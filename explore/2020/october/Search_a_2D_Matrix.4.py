'''
You are here!
Your runtime beats 91.19 % of python submissions.
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if 0 == len(matrix) or 0 == len(matrix[0]):  # []  [[]]
            return False
        
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        if 0 == hi:
            return matrix[0][0] == target
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            mid_i, mid_j = divmod(mid, n)
            if target == matrix[mid_i][mid_j]:
                return True
            elif target > matrix[mid_i][mid_j]:
                lo = mid + 1
            else:
                hi = mid - 1
            
        return False