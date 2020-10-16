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
        if not matrix:
            return False
        if len(matrix[0]) == 0:
            return False
        
        array = []
        for sub_array in matrix:
            array += sub_array

        if target in array:
            return True
        else:
            return False