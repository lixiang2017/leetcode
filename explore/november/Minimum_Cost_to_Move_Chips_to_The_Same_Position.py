'''
You are here!
Your runtime beats 100.00 % of python submissions.
'''




class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        odd = even = 0
        for pos in position:
            if pos & 1:
                odd += 1
            else:
                even += 1
        
        return min(odd, even)
    