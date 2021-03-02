'''
You are here!
Your runtime beats 90.85 % of python submissions.
'''


class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([a * a for a in A])