'''
Time: O(32) = O(1)
Space: O(1)

You are here!
Your runtime beats 12.28 % of python submissions.
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        while n:
            if n & 1: num += 1
            n >>= 1
            
        return num


'''
You are here!
Your runtime beats 33.62 % of python submissions.
You are here!
Your memory usage beats 68.32 % of python submissions.
'''


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        while n:
            total += n & 1
            n >>= 1
        
        return total
