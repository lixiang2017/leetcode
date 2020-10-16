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
        
        m = len(matrix)
        index = 0
        while index < m and matrix[index][-1] < target:
            index += 1
            
        return target in matrix[index] if index < m else False
        