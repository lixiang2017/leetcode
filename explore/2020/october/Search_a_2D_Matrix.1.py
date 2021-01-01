'''
You are here!
Your runtime beats 98.73 % of python submissions.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == [[]] or matrix == []:
            return False
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        target_row = None
        for r in xrange(rows):
            if matrix[r][0] == target:
                return True
            elif target > matrix[r][0]:
                target_row = r
            else:
                break
                
        if target_row is None:
            return False
        
        for c in range(1, cols):
            if matrix[target_row][c] == target:
                return True
        return False
    