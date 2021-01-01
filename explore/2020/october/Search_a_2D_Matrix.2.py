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
        
        for row in matrix:
            if len(row) < 1:   # for matrix == [[]]
                return False
            
            if row[-1] == target:
                return True
            elif row[-1] > target:
                for element in row:
                    if element == target:
                        return True
        return False
                