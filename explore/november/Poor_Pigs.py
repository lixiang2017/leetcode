'''
You are here!
Your runtime beats 100.00 % of python submissions.
'''

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        pigs = 0
        rounds = minutesToTest / minutesToDie
        while (rounds + 1) ** pigs < buckets:
            pigs += 1
        
        return pigs