'''
approach: Bit Manipulation
Time: O(32) = O(1)
Space: O(1)

trick: n &= n - 1  -> remove Low Significant 1

You are here!
Your runtime beats 33.62 % of python submissions.
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        while n:
            n &= n - 1
            num += 1
            
        return num
